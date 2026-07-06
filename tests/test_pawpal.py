from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete_changes_status():
    task = Task(description="Morning walk", time="7:00 AM", frequency="daily")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3, weight=65.0)
    assert len(pet.tasks) == 0
    pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily"))
    assert len(pet.tasks) == 1


def make_scheduler():
    owner = Owner(name="Alex", email="alex@example.com", phone="555-1234")
    pet = Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3, weight=65.0)
    owner.add_pet(pet)
    return owner, pet, Scheduler(owner)


# --- Sorting Correctness ---

def test_sort_by_time_orders_chronologically():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Dinner", time="6:00 PM", frequency="daily"))
    pet.add_task(Task(description="Breakfast", time="8:00 AM", frequency="daily"))
    pet.add_task(Task(description="Walk", time="1:00 PM", frequency="daily"))

    sorted_tasks = scheduler.sort_by_time(pet.tasks)

    assert [t.description for t in sorted_tasks] == ["Breakfast", "Walk", "Dinner"]


def test_sort_by_time_handles_midnight_and_noon_boundary():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Noon feeding", time="12:00 PM", frequency="daily"))
    pet.add_task(Task(description="Midnight check", time="12:00 AM", frequency="daily"))
    pet.add_task(Task(description="Morning walk", time="8:00 AM", frequency="daily"))

    sorted_tasks = scheduler.sort_by_time(pet.tasks)

    assert [t.description for t in sorted_tasks] == [
        "Midnight check", "Morning walk", "Noon feeding",
    ]


def test_sort_by_time_does_not_mutate_original_list():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Dinner", time="6:00 PM", frequency="daily"))
    pet.add_task(Task(description="Breakfast", time="8:00 AM", frequency="daily"))
    original_order = list(pet.tasks)

    scheduler.sort_by_time(pet.tasks)

    assert pet.tasks == original_order


# --- Recurrence Logic ---

def test_complete_daily_task_creates_next_day_occurrence():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily", date="2026-01-01"))

    result = scheduler.complete_task("Buddy", "Feed breakfast")

    assert result is True
    assert len(pet.tasks) == 2
    original, next_occurrence = pet.tasks
    assert original.completed is True
    assert next_occurrence.completed is False
    assert next_occurrence.date == "2026-01-02"
    assert next_occurrence.description == "Feed breakfast"
    assert next_occurrence.time == "8:00 AM"
    assert next_occurrence.frequency == "daily"


def test_complete_weekly_task_creates_next_week_occurrence():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Grooming", time="10:00 AM", frequency="weekly", date="2026-01-01"))

    scheduler.complete_task("Buddy", "Grooming")

    assert len(pet.tasks) == 2
    next_occurrence = pet.tasks[1]
    assert next_occurrence.date == "2026-01-08"
    assert next_occurrence.completed is False


def test_complete_monthly_task_does_not_recur():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Vet visit", time="9:00 AM", frequency="monthly", date="2026-01-01"))

    result = scheduler.complete_task("Buddy", "Vet visit")

    assert result is True
    assert len(pet.tasks) == 1
    assert pet.tasks[0].completed is True


def test_complete_task_returns_false_for_unknown_pet_or_task():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily"))

    assert scheduler.complete_task("Unknown Pet", "Feed breakfast") is False
    assert scheduler.complete_task("Buddy", "Nonexistent task") is False


# --- Conflict Detection ---

def test_detect_conflicts_flags_duplicate_times_for_same_pet():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily", date="2026-01-01"))
    pet.add_task(Task(description="Give medication", time="8:00 AM", frequency="daily", date="2026-01-01"))

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    assert "Buddy" in warnings[0]
    assert "8:00 AM" in warnings[0]
    assert "Feed breakfast" in warnings[0]
    assert "Give medication" in warnings[0]


def test_detect_conflicts_ignores_same_time_on_different_pets():
    owner, pet, scheduler = make_scheduler()
    other_pet = Pet(name="Max", species="Cat", breed="Tabby", age=2, weight=10.0)
    owner.add_pet(other_pet)
    pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily", date="2026-01-01"))
    other_pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily", date="2026-01-01"))

    warnings = scheduler.detect_conflicts()

    assert warnings == []


def test_detect_conflicts_returns_empty_when_no_overlap():
    _, pet, scheduler = make_scheduler()
    pet.add_task(Task(description="Feed breakfast", time="8:00 AM", frequency="daily"))
    pet.add_task(Task(description="Walk", time="1:00 PM", frequency="daily"))

    assert scheduler.detect_conflicts() == []
