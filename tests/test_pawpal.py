from pawpal_system import Task, Pet


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
