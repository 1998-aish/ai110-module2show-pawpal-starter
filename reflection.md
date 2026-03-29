# PawPal+ Project Reflection

## 1. System Design
1. A user should be able to add a pet with details like name, type, and age.
2. A user should be able to schedule activities such as walks or feeding times for their pets.
3. A user should be able to view all upcoming tasks for their pets in one place.

## Building Blocks

### 1. Pet
Attributes:
- id
- name
- type
- age
- ownerId

Methods:
- addPet()
- updatePet()
- deletePet()

---

### 2. Task
Attributes:
- id
- petId
- type (walk, feed, vet)
- dateTime
- status

Methods:
- createTask()
- markComplete()
- getTasksForToday()

---

### 3. User
Attributes:
- id
- name
- email

Methods:
- createUser()
- login()

**a. Initial design**

I designed the system using three main classes: User, Pet, and Task.

The User class represents the pet owner and stores basic information such as id, name, and email. It is responsible for user-related actions like account creation and login.

The Pet class represents individual pets owned by a user. It stores details like name, type, age, and owner_id. This class is responsible for managing pet-related actions such as adding, updating, and deleting pets.

The Task class represents activities associated with a pet, such as walking or feeding. It includes attributes like type, date_time, and status. This class is responsible for creating tasks, marking them as complete, and retrieving daily tasks.

The relationships between these classes are such that a User can have multiple Pets, and each Pet can have multiple Tasks.

**b. Design changes**

After reviewing the initial design, I made a few refinements to improve clarity and structure.

First, I improved the relationship between the User and Pet classes. Initially, the connection was only represented using an owner_id in the Pet class. I recognized that a user can own multiple pets, so I considered how this relationship could be more explicitly represented in the system design.

Second, I reviewed the placement of certain methods. For example, the get_tasks_for_today() method was originally included in the Task class. I realized that this type of functionality may be better suited for a higher-level service or manager class, since it involves filtering across multiple tasks rather than behavior of a single task. However, I kept it in the Task class for simplicity at this stage.

These refinements helped me better understand how to separate responsibilities and design a system that can scale more effectively in the future.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers several basic constraints to organize tasks effectively.

First, time is the primary constraint. Tasks are scheduled and sorted based on their assigned time so that the user can clearly see the order of activities throughout the day.

Second, completion status is considered. The system allows filtering of tasks based on whether they are completed or pending, helping the user focus on what still needs to be done.

Third, pet-specific grouping is supported. Tasks are associated with individual pets, allowing the user to view and manage tasks for each pet separately.

In terms of priorities, time was given the highest importance because scheduling is fundamentally about organizing tasks in a time-based order. Other factors like priority levels (low, medium, high) are captured in the data but are not yet actively used in decision-making.

The design focuses on simplicity and clarity, ensuring that tasks are easy to view, manage, and understand for the user.

**b. Tradeoffs**


One tradeoff in my scheduler design is how task conflicts are detected.

Currently, the system only checks for exact time matches between tasks. This means it will detect conflicts only when two tasks are scheduled at the exact same time, but it does not account for overlapping durations (for example, a 30-minute task overlapping with another task starting within that time window).

This approach keeps the implementation simple and easy to understand, but it limits the accuracy of conflict detection in more realistic scenarios.

Additionally, while a more optimized approach using a dictionary can improve performance, I chose to keep a simpler loop-based implementation for readability and clarity at this stage.

---

## 3. AI Collaboration

**a. How you used AI**

I used VS Code Copilot throughout the project to assist with different stages of development. It was most helpful during the design and implementation phases, especially for generating class structures, writing methods, and creating test cases.

Copilot Chat helped me brainstorm ideas for improving the scheduler, such as adding sorting, filtering, recurring tasks, and conflict detection. The inline suggestions were also useful for writing clean Python code quickly, particularly when working with list comprehensions and datetime logic.

Using separate chat sessions for different phases (design, implementation, testing) helped me stay organized and focused. It allowed me to clearly separate concerns and avoid mixing ideas from different stages of the project.


**b. Judgment and verification**

Although Copilot was very helpful, I did not blindly accept all suggestions. For example, during conflict detection, Copilot suggested returning formatted strings, but I chose to return Task objects instead. This made the design more flexible and aligned better with the rest of my system.

I also reviewed and tested all generated code to ensure it worked correctly with my existing implementation. In some cases, I simplified AI-generated code to improve readability and maintain consistency.

Through this process, I learned that while AI can accelerate development, it is important to act as the "lead architect" by making final decisions about design, structure, and tradeoffs. AI is a powerful assistant, but the responsibility for building a clean and logical system remains with the developer.

---

## 4. Testing and Verification

**a. What you tested**
I tested both normal functionality (happy paths) and edge cases of the scheduler system.

### Happy Paths
- Tasks are correctly sorted in ascending order based on time.
- Filtering by pet returns only the selected pet’s tasks.
- Filtering by status returns only completed or pending tasks as expected.
- Completing a daily or weekly task correctly generates a new task with the next occurrence.
- Conflict detection correctly identifies tasks scheduled at the same time.

### Edge Cases
- A pet with no tasks returns an empty list without errors.
- Tasks added out of order are still sorted correctly.
- Two tasks scheduled at the exact same time are detected as a conflict.
- Filtering for a non-existent pet returns an empty result.
- Completing a one-time task does not generate a new task.

**b. Confidence**

I am fairly confident that the scheduler works correctly for its core functionality. The automated tests verify key behaviors such as sorting tasks by time, filtering by pet and status, handling recurring tasks, and detecting conflicts when tasks occur at the same time.

However, there are still some edge cases that could be explored further. For example, I would like to test overlapping task durations rather than just exact time matches, as well as more complex recurrence patterns such as monthly schedules.

Additionally, I would test scenarios involving multiple pets with a large number of tasks to ensure the system performs efficiently and remains accurate under heavier usage.

---

## 5. Reflection

### a. What went well

The part I am most satisfied with is how the overall system came together from design to implementation. I was able to successfully translate the UML diagram into working Python classes and then connect that logic to the Streamlit UI. Features like sorting tasks, handling recurring tasks, and detecting conflicts worked as expected and made the application feel more realistic and complete.

---

### b. What you would improve

If I had another iteration, I would improve the scheduling logic to handle more complex scenarios such as overlapping task durations instead of only exact time matches. I would also enhance the user interface by allowing users to manage multiple pets more interactively and edit or delete tasks. Additionally, I would expand test coverage to include more edge cases and improve the overall robustness of the system.

---

### c. Key takeaway

One important thing I learned is that designing a system requires careful planning and decision-making, especially when working with AI tools. While AI can generate useful suggestions and speed up development, it is important to think critically and make intentional design choices. Acting as the "lead architect" helped me ensure that the system remained clean, consistent, and aligned with the project goals.