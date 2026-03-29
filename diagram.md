classDiagram
    direction LR

    class User {
        +int id
        +string name
        +string email
        +createUser()
        +login()
    }

    class Pet {
        +int id
        +string name
        +string type
        +int age
        +int ownerId
        +addPet()
        +updatePet()
        +deletePet()
    }

    class Task {
        +int id
        +int petId
        +string type
        +datetime dateTime
        +string status
        +createTask()
        +markComplete()
        +getTasksForToday()
    }

    User "1" -- "0..*" Pet : owns >
    Pet "1" -- "0..*" Task : has >