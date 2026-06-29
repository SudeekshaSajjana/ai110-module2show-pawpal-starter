from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str  # e.g. "daily", "weekly", "monthly"
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def reset(self) -> None:
        """Reset this task back to incomplete."""
        self.completed = False

    def get_summary(self) -> str:
        """Return a formatted one-line summary of the task and its status."""
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description} at {self.time} ({self.frequency})"


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    weight: float
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet's task list if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_pending_tasks(self) -> List[Task]:
        """Return all tasks that have not yet been completed."""
        return [t for t in self.tasks if not t.completed]

    def get_profile(self) -> str:
        """Return a formatted summary of this pet's details."""
        return (
            f"Name: {self.name} | Species: {self.species} | Breed: {self.breed} | "
            f"Age: {self.age} yrs | Weight: {self.weight} lbs"
        )


class Owner:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's list if it exists."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return a flat list of every task across all of this owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def get_contact_info(self) -> str:
        """Return a formatted string of the owner's contact details."""
        return f"{self.name} | Email: {self.email} | Phone: {self.phone}"


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks across every pet owned."""
        return [t for t in self.owner.get_all_tasks() if not t.completed]

    def get_tasks_by_frequency(self, frequency: str) -> List[Task]:
        """Return all tasks matching the given frequency (e.g. 'daily', 'weekly')."""
        return [
            t for t in self.owner.get_all_tasks()
            if t.frequency.lower() == frequency.lower()
        ]

    def get_tasks_for_pet(self, pet_name: str) -> Optional[List[Task]]:
        """Return the task list for a named pet, or None if the pet is not found."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                return pet.tasks
        return None

    def complete_task(self, pet_name: str, task_description: str) -> bool:
        """Mark a specific task complete for a named pet; returns True on success."""
        tasks = self.get_tasks_for_pet(pet_name)
        if tasks is None:
            return False
        for task in tasks:
            if task.description.lower() == task_description.lower():
                task.mark_complete()
                return True
        return False

    def get_daily_schedule(self) -> str:
        """Return a formatted string of all daily tasks across every pet."""
        daily_tasks = self.get_tasks_by_frequency("daily")
        if not daily_tasks:
            return "No daily tasks scheduled."
        lines = ["--- Daily Schedule ---"]
        for task in daily_tasks:
            lines.append(task.get_summary())
        return "\n".join(lines)
