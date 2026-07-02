from pawpal_system import Task, Pet, Owner, Scheduler


# --- Setup Owner ---
owner = Owner(name="Alex Rivera", email="alex@email.com", phone="555-0192")

# --- Create Pets ---
buddy = Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3, weight=65.0)
luna = Pet(name="Luna", species="Cat", breed="Siamese", age=5, weight=9.5)

# --- Buddy's tasks (Evening walk intentionally clashes with Feed dinner) ---
buddy.add_task(Task(description="Morning walk",   time="7:00 AM",  frequency="daily",  date="2026-06-30"))
buddy.add_task(Task(description="Feed breakfast", time="8:00 AM",  frequency="daily",  date="2026-06-30"))
buddy.add_task(Task(description="Evening walk",   time="6:00 PM",  frequency="daily",  date="2026-06-30"))
buddy.add_task(Task(description="Feed dinner",    time="6:00 PM",  frequency="daily",  date="2026-06-30"))  # conflict!

# --- Luna's tasks (no conflicts) ---
luna.add_task(Task(description="Feed breakfast",  time="8:30 AM",  frequency="daily",  date="2026-06-30"))
luna.add_task(Task(description="Clean litter box",time="12:00 PM", frequency="daily",  date="2026-06-30"))
luna.add_task(Task(description="Brush fur",       time="5:00 PM",  frequency="weekly", date="2026-06-30"))

owner.add_pet(buddy)
owner.add_pet(luna)

scheduler = Scheduler(owner)

# ── Run conflict detection ─────────────────────────────────────────────────────
print("=" * 50)
print("  Conflict Detection")
print("=" * 50)
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        print(f"  {warning}")
else:
    print("  No conflicts found.")

# ── Full schedule (sorted) ─────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("  Today's Full Schedule (sorted by time)")
print("=" * 50)
for task in scheduler.sort_by_time(owner.get_all_tasks()):
    print(f"  {task.get_summary()}")
