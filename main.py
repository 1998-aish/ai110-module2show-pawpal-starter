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
    from datetime import datetime, timedelta

    from datetime import datetime

    same_time = datetime.now()

    task1 = Task(
        description="Walk dog",
        time=same_time,
        frequency="daily"
    )

    task2 = Task(
        description="Feed cat",
        time=same_time,   # same time → conflict
        frequency="daily"
    )

    task3 = Task(
        description="Midday play",
        time=datetime.now() + timedelta(hours=3),
        frequency="daily"
    )
    # Mark one task complete
    new_task = task1.mark_complete()

    # If recurring → add new instance
    if new_task:
        dog.add_task(new_task)

    # Assign tasks to pets
    dog.add_task(task1)
    cat.add_task(task2)
    dog.add_task(task3)

    # Create scheduler
    scheduler = Scheduler(owner)

    # Print today's schedule
    print("\n🐾 Today's Schedule:\n")

    all_tasks = scheduler.get_all_tasks()

    print("\n--- All Tasks (Unsorted) ---")
    for t in all_tasks:
        print(t.description, t.time.strftime("%H:%M"))

    # SORTED
    sorted_tasks = scheduler.sort_by_time(all_tasks)

    print("\n--- Sorted Tasks ---")
    for t in sorted_tasks:
        print(t.description, t.time.strftime("%H:%M"))

    # FILTER: Pending tasks
    pending_tasks = scheduler.filter_by_status(False)

    print("\n--- Pending Tasks ---")
    for t in pending_tasks:
        print(t.description)

    # FILTER: By pet
    pet_tasks = scheduler.filter_by_pet("Buddy")

    print("\n--- Tasks for Buddy ---")
    for t in pet_tasks:
        print(t.description)


    conflicts = scheduler.detect_conflicts()

    print("\n--- Conflict Check ---")
    if conflicts:
        for t1, t2 in conflicts:
            print(f"Conflict: '{t1.description}' and '{t2.description}' are within 30 minutes of each other")
    else:
        print("No conflicts found.")

if __name__ == "__main__":
    main()