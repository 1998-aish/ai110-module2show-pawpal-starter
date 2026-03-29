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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
