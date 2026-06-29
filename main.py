from pawpal_system import Task, Pet, Owner, Scheduler


# --- Setup Owner ---
owner = Owner(name="Alex Rivera", email="alex@email.com", phone="555-0192")

# --- Create Pets ---
buddy = Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3, weight=65.0)
luna = Pet(name="Luna", species="Cat", breed="Siamese", age=5, weight=9.5)

# --- Create Tasks for Buddy ---
buddy.add_task(Task(description="Morning walk",     time="7:00 AM",  frequency="daily"))
buddy.add_task(Task(description="Feed breakfast",   time="8:00 AM",  frequency="daily"))
buddy.add_task(Task(description="Evening walk",     time="6:00 PM",  frequency="daily"))

# --- Create Tasks for Luna ---
luna.add_task(Task(description="Feed breakfast",    time="8:30 AM",  frequency="daily"))
luna.add_task(Task(description="Clean litter box",  time="12:00 PM", frequency="daily"))
luna.add_task(Task(description="Brush fur",         time="5:00 PM",  frequency="weekly"))

# --- Register Pets with Owner ---
owner.add_pet(buddy)
owner.add_pet(luna)

# --- Run Scheduler ---
scheduler = Scheduler(owner)

print("=" * 40)
print("        PawPal — Today's Schedule")
print("=" * 40)

for pet in owner.pets:
    print(f"\n{pet.name} ({pet.breed})")
    print("-" * 30)
    pending = pet.get_pending_tasks()
    if pending:
        for task in pending:
            print(f"  {task.get_summary()}")
    else:
        print("  All tasks complete!")

print("\n" + "=" * 40)
print(f"Total pending tasks: {len(scheduler.get_all_pending_tasks())}")
print("=" * 40)
