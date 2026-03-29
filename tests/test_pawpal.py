from datetime import datetime,timedelta
from pawpal_system import Task, Pet


# ---------------- TEST 1 ----------------
def test_task_completion():
    task = Task(
        description="Test task",
        time=datetime.now(),
        frequency="daily"
    )

    # Before completion
    assert task.completed == False

    # Mark complete
    task.mark_complete()

    # After completion
    assert task.completed == True


# ---------------- TEST 2 ----------------
def test_add_task_to_pet():
    pet = Pet(name="Buddy", type="Dog", age=3)

    task = Task(
        description="Walk dog",
        time=datetime.now(),
        frequency="daily"
    )

    # Initially no tasks
    assert len(pet.get_tasks()) == 0

    # Add task
    pet.add_task(task)

    # Now should have 1 task
    assert len(pet.get_tasks()) == 1