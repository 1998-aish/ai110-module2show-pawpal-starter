from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


# ---------------- SORTING TEST ----------------
def test_sorting_tasks_by_time():
    owner = Owner(name="Test")
    pet = Pet(name="Buddy", type="Dog", age=3)
    owner.add_pet(pet)

    # Create tasks out of order
    t1 = Task("Late", datetime.now() + timedelta(hours=3), "daily")
    t2 = Task("Early", datetime.now() + timedelta(hours=1), "daily")
    t3 = Task("Middle", datetime.now() + timedelta(hours=2), "daily")

    pet.add_task(t1)
    pet.add_task(t2)
    pet.add_task(t3)

    scheduler = Scheduler(owner)

    sorted_tasks = scheduler.sort_by_time(pet.get_tasks())

    # Check order
    assert sorted_tasks[0].description == "Early"
    assert sorted_tasks[1].description == "Middle"
    assert sorted_tasks[2].description == "Late"


# ---------------- RECURRENCE TEST ----------------
def test_daily_task_recurrence():
    task = Task(
        description="Walk",
        time=datetime.now(),
        frequency="daily"
    )

    new_task = task.mark_complete()

    # Should create a new task
    assert new_task is not None

    # New task should be 1 day later
    assert new_task.time.date() == (task.time + timedelta(days=1)).date()


# ---------------- CONFLICT DETECTION TEST ----------------
def test_conflict_detection():
    owner = Owner(name="Test")
    pet = Pet(name="Buddy", type="Dog", age=3)
    owner.add_pet(pet)

    same_time = datetime.now()

    t1 = Task("Walk", same_time, "daily")
    t2 = Task("Feed", same_time, "daily")

    pet.add_task(t1)
    pet.add_task(t2)

    scheduler = Scheduler(owner)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) > 0

    t1_conflict, t2_conflict = conflicts[0]
    assert t1_conflict.description == "Walk"
    assert t2_conflict.description == "Feed"