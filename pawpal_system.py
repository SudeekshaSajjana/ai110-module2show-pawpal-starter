from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str  # e.g. "daily", "weekly", "monthly"
    completed: bool = False
    date: Optional[str] = None  # "YYYY-MM-DD"; None means undated

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def reset(self) -> None:
        """Reset this task back to incomplete."""
        self.completed = False

    def get_summary(self) -> str:
        """Return a formatted one-line summary of the task and its status."""
        status = "Done" if self.completed else "Pending"
        date_str = f" on {self.date}" if self.date else ""
        return f"[{status}] {self.description} at {self.time}{date_str} ({self.frequency})"


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
        """Mark a specific task complete for a named pet; returns True on success.

        For daily and weekly tasks, automatically schedules the next occurrence.
        """
        pet = next(
            (p for p in self.owner.pets if p.name.lower() == pet_name.lower()), None
        )
        if pet is None:
            return False
        for task in pet.tasks:
            if task.description.lower() == task_description.lower():
                task.mark_complete()
                self._schedule_next(pet, task)
                return True
        return False

    def _schedule_next(self, pet: Pet, task: Task) -> None:
        """Add the next occurrence of a recurring task to the pet's schedule.

        Supports daily (+1 day) and weekly (+7 days) frequencies. Monthly tasks
        are skipped. If the completed task has no date, today is used as the base.

        Args:
            pet:  The Pet whose task list receives the new occurrence.
            task: The just-completed Task whose recurrence pattern is copied.
        """
        days = {"daily": 1, "weekly": 7}
        if task.frequency not in days:
            return
        base = datetime.strptime(task.date, "%Y-%m-%d") if task.date else datetime.today()
        next_date = (base + timedelta(days=days[task.frequency])).strftime("%Y-%m-%d")
        pet.add_task(Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            date=next_date,
        ))

    def get_daily_schedule(self) -> str:
        """Return a formatted string of all daily tasks across every pet."""
        daily_tasks = self.get_tasks_by_frequency("daily")
        if not daily_tasks:
            return "No daily tasks scheduled."
        lines = ["--- Daily Schedule ---"]
        for task in daily_tasks:
            lines.append(task.get_summary())
        return "\n".join(lines)

    def detect_conflicts(self) -> List[str]:
        """Return warning strings for any same-pet, same-time, same-date task overlaps.

        Groups each pet's tasks by (time, date) in a single pass, then reports
        any slot with more than one task in one combined message. Handles three
        or more tasks at the same slot rather than emitting pairwise warnings.

        Returns:
            A list of human-readable warning strings, one per conflicting slot.
            Returns an empty list when no conflicts exist. Never raises.
        """
        warnings = []
        for pet in self.owner.pets:
            time_slots = defaultdict(list)
            for task in pet.tasks:
                time_slots[(task.time, task.date)].append(task.description)
            for (time, date), descriptions in time_slots.items():
                if len(descriptions) > 1:
                    date_info = f" on {date}" if date else ""
                    names = " and ".join(f'"{d}"' for d in descriptions)
                    warnings.append(
                        f"WARNING: {pet.name} has a time conflict at {time}{date_info} — {names}"
                    )
        return warnings

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Return a new list of tasks sorted chronologically by their time attribute.

        Parses each task's time string (e.g. "8:00 AM") once via strptime and
        uses the result as the sort key, so no repeated parsing happens per pair.

        Args:
            tasks: Any list of Task objects — pending, completed, or mixed.

        Returns:
            A new sorted list; the original list is not modified.
        """
        return sorted(tasks, key=lambda t: datetime.strptime(t.time, "%I:%M %p"))

    def filter_tasks(
        self,
        completed: Optional[bool] = None,
        pet_names: Optional[List[str]] = None,
    ) -> List[Task]:
        """Return tasks filtered by completion status and/or pet name.

        Both filters are optional and can be combined freely.

        Args:
            completed:  True  → only completed tasks.
                        False → only pending tasks.
                        None  → all tasks regardless of status (default).
            pet_names:  Restrict results to these pets (case-insensitive).
                        None means all pets are included (default).

        Returns:
            A flat list of matching Task objects. Returns an empty list if
            no tasks match — never returns None.
        """
        names_lower = {n.lower() for n in pet_names} if pet_names else None

        results = []
        for pet in self.owner.pets:
            if names_lower and pet.name.lower() not in names_lower:
                continue
            for task in pet.tasks:
                if completed is not None and task.completed != completed:
                    continue
                results.append(task)
        return results
