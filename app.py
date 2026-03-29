import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

# ---------------- SESSION SETUP ----------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Vivek")

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+!

Manage your pets and their daily care tasks easily.
"""
)

# ---------------- INPUT SECTION ----------------
st.subheader("Add Pet & Tasks")

owner_name = st.text_input("Owner name", value="Vivek")
pet_name = st.text_input("Pet name", value="Buddy")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Add Task")

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)

with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=1)

owner = st.session_state.owner

# ---------------- ADD TASK ----------------
if st.button("Add task"):
    pets = owner.get_pets()

    if pets:
        pet = pets[0]
    else:
        pet = Pet(name=pet_name, type=species, age=1)
        owner.add_pet(pet)

    task = Task(
        description=task_title,
        time=datetime.now(),
        frequency="daily"
    )

    pet.add_task(task)
    st.success("Task added!")

# ---------------- DISPLAY CURRENT TASKS ----------------
pets = owner.get_pets()

if pets:
    tasks = pets[0].get_tasks()
    if tasks:
        st.write("### Current Tasks")
        for t in tasks:
            st.write(f"- {t.description}")
    else:
        st.info("No tasks yet. Add one above.")
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# ---------------- SCHEDULER ----------------
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    owner = st.session_state.owner
    scheduler = Scheduler(owner)

    # Get today's tasks
    tasks_today = scheduler.get_tasks_for_today()

    # Sort tasks
    sorted_tasks = scheduler.sort_by_time(tasks_today)

    st.write("### Today's Schedule")

    if sorted_tasks:
        for task in sorted_tasks:
            if task.completed:
                st.success(f"{task.description} at {task.time.strftime('%H:%M')}")
            else:
                st.write(f"{task.description} at {task.time.strftime('%H:%M')}")
    else:
        st.info("No tasks scheduled for today.")

    # ---------------- CONFLICT DETECTION ----------------
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        st.warning("⚠️ Task conflicts detected!")

        for t1, t2 in conflicts:
            st.write(
                f"Conflict between '{t1.description}' and '{t2.description}' at {t1.time.strftime('%H:%M')}"
            )