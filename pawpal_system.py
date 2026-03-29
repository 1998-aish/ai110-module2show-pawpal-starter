from dataclasses import dataclass
from datetime import datetime
from typing import List

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def create_user(self) -> None:
        pass

    def login(self) -> None:
        pass


@dataclass
class Pet:
    id: int
    name: str
    type: str
    age: int
    owner_id: int

    def add_pet(self) -> None:
        pass

    def update_pet(self) -> None:
        pass

    def delete_pet(self) -> None:
        pass


@dataclass
class Task:
    id: int
    pet_id: int
    type: str
    date_time: datetime
    status: str

    def create_task(self) -> None:
        pass

    def mark_complete(self) -> None:
        pass

    @staticmethod
    def get_tasks_for_today(tasks: List["Task"]) -> List["Task"]:
        pass