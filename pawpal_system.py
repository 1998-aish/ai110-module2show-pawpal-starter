from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Tuple


@dataclass
class Owner:
    name: str
    pets: List["Pet"] = field(default_factory=list)

    def add_pet(self, pet: "Pet"):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_pets(self) -> List["Pet"]:
        """Return all pets owned."""
        return self.pets


@dataclass
class Pet:
    name: str
    type: str
    age: int
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task"):
        """Add a task to the pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List["Task"]:
        """Return all tasks for the pet."""
        return self.tasks


@dataclass
class Task:
    description: str
    time: datetime   
    frequency: str
    completed: bool = False

    def mark_complete(self):
        """Mark task complete and create next occurrence if recurring."""
        self.completed = True

    # Handle recurring tasks
        if self.frequency == "daily":
            new_time = self.time + timedelta(days=1)
        elif self.frequency == "weekly":
            new_time = self.time + timedelta(weeks=1)
        else:
            return None

        return Task(
            description=self.description,
            time=new_time,
            frequency=self.frequency
        )


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from all pets."""
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return tasks
    def filter_by_status(self, completed: bool):
        """Return tasks filtered by completion status (completed or pending)."""
        return [t for t in self.get_all_tasks() if t.completed == completed]

    def filter_by_pet(self, pet_name: str):
        """Return all tasks belonging to a specific pet."""
        result = []
        for pet in self.owner.get_pets():
            if pet.name == pet_name:
                result.extend(pet.get_tasks())
        return result
    def sort_by_time(self, tasks):
        """Return tasks sorted by their scheduled time."""
        return sorted(tasks, key=lambda t: t.time)
    def detect_conflicts(self, window_minutes: int = 30) -> List[Tuple[Task, Task]]:
        """Detect tasks scheduled at the same time and return warning messages."""
        tasks = sorted(self.get_tasks_for_today(), key=lambda t: t.time)
        return [
            (tasks[i], tasks[i + 1])
            for i in range(len(tasks) - 1)
            if tasks[i + 1].time - tasks[i].time < timedelta(minutes=window_minutes)
        ]

    def get_tasks_for_today(self) -> List[Task]:
        """Return tasks scheduled for today, including recurring ones, sorted by time."""
        today = datetime.now().date()
        result = []
        for t in self.get_all_tasks():
            if t.time.date() == today:
                result.append(t)
            elif t.frequency == "daily":
                result.append(t)
            elif t.frequency == "weekly" and t.time.weekday() == today.weekday():
                result.append(t)
        return sorted(result, key=lambda t: t.time)

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks."""
        return [t for t in self.get_all_tasks() if not t.completed]

    def get_tasks_for_pet(self, pet_name: str) -> List[Task]:
        """Return all tasks for a specific pet, sorted by time."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                return sorted(pet.tasks, key=lambda t: t.time)
        return []

    def get_conflicts(self, window_minutes: int = 30) -> List[Tuple[Task, Task]]:
        """Return pairs of today's tasks that are within window_minutes of each other."""
        tasks = self.get_tasks_for_today()
        conflicts = []
        for i in range(len(tasks) - 1):
            gap = tasks[i + 1].time - tasks[i].time
            if gap < timedelta(minutes=window_minutes):
                conflicts.append((tasks[i], tasks[i + 1]))
        return conflicts