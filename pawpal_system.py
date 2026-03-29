from dataclasses import dataclass, field
from datetime import datetime
from typing import List


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
        """Mark the task as completed."""
        self.completed = True


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from all pets."""
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return tasks

    def get_tasks_for_today(self) -> List[Task]:
        """Return tasks scheduled for today."""
        today = datetime.now().date()
        return [t for t in self.get_all_tasks() if t.time.date() == today]

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks."""
        return [t for t in self.get_all_tasks() if t.status != "completed"]