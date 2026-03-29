from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create an owner
    owner = Owner(name="Vivek")

    # Create pets
    dog = Pet(name="Buddy", type="Dog", age=3)
    cat = Pet(name="Whiskers", type="Cat", age=2)

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create tasks with different times
    task1 = Task(
        description="Morning walk",
        time=datetime.now(),
        frequency="daily"
    )

    task2 = Task(
        description="Feed cat",
        time=datetime.now() + timedelta(hours=2),
        frequency="daily"
    )

    task3 = Task(
        description="Vet appointment",
        time=datetime.now() + timedelta(days=1),
        frequency="once"
    )

    # Assign tasks to pets
    dog.add_task(task1)
    cat.add_task(task2)
    dog.add_task(task3)

    # Create scheduler
    scheduler = Scheduler(owner)

    # Print today's schedule
    print("\n🐾 Today's Schedule:\n")

    tasks_today = scheduler.get_tasks_for_today()

    if not tasks_today:
        print("No tasks for today.")
    else:
        for task in tasks_today:
            status = "✅ Done" if task.completed else "⏳ Pending"
            print(f"- {task.description} at {task.time.strftime('%H:%M')} [{status}]")


if __name__ == "__main__":
    main()