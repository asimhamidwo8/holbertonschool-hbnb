# HBnB Evolution – Project Documentation

---

## 📘 Introduction

**HBnB Evolution** is a simplified based on Airbnb application. 

This app allows users to:
* Create and manage accounts.
* List places for rent.
* Add amenities to places.
* Write reviews for places they visited.

This document serves as the main blueprint for the project and includes:
1. **Package Diagram:** The overall system architecture.
2. **Class Diagram:** The database entities and relationships.
3. **Sequence Diagrams:** The step-by-step flow for API requests.

---

## 🧱 High-Level Architecture – Package Diagram



<img width="497" height="780" alt="image" src="https://github.com/user-attachments/assets/d3e94a74-fcc4-4361-9281-975201729708" />


### Architectural Layers:
1. **Presentation Layer:** Contains the `API` and `Services`. It acts as the entry point for the application, handling incoming client requests.
2. **BusinessLogic Layer:** Contains the core models (`User`, `Place`, `Review`, `Amenity`). It receives requests from the Presentation Layer via the **Facade Pattern**, processes business rules, and ensures data integrity.
3. **Persistence Layer:** Contains the `Database` and `Repository`. It handles data storage, retrieval, and database operations based on commands from the Business Logic Layer.

---

## 🏛️ Detailed Class Diagram

```mermaid
---
config:
    layout: elk
---
classDiagram
    class User {
        +id: UUID
        +first_name: String
        +last_name: String
        +email: String
        -password: String
        +is_admin: Boolean
        +is_owner: Boolean
        +created_at: DateTime
        +updated_at: DateTime
        +register()
        +update_profile()
        +delete()
    }
    class Place {
        +id: UUID
        +title: String
        +description: String
        +price: Float
        +latitude: Float
        +longitude: Float
        +owner_id: UUID
        +created_at: DateTime
        +updated_at: DateTime
        +create()
        +update()
        +delete()
        +list()
    }
    class Review {
        +id: UUID
        +place_id: UUID
        +user_id: UUID
        +rating: Integer
        +comment: String
        +created_at: DateTime
        +updated_at: DateTime
        +create()
        +update()
        +delete()
        +list_by_place()
    }
    class Amenity {
        +id: UUID
        +name: String
        +description: String
        +created_at: DateTime
        +updated_at: DateTime
        +create()
        +update()
        +delete()
        +list()
    }
    User "1" --> "n" Place : owns
    User "1" o-- "n" Review : writes
    Place "1" *-- "n" Review : has
    Place "n" o-- "n" Amenity : includes
```

---

## 🔁 Sequence Diagrams – API Interaction Flow

## The following diagrams illustrate the step-by-step interactions between the layers (User -> API -> BusinessLogic -> Persistence) for four core operations.



### 1. User Registration

```mermaid
sequenceDiagram
  actor A1 as User
  participant API as Presentation (API)
  participant BusinessLogic
  participant Persistence as Persistence (Database)


A1 ->> API: User Register Request (first_name, last_name, email, password)
Note over API: Validate and Process Request 
API ->> BusinessLogic: Forward Register Request 
Note over BusinessLogic: Hash password, Generate UUID, Create Time
BusinessLogic ->> Persistence: Save user data (ID, first_name, last_name, email, hach_password, created_at, update_at)
Persistence -->> BusinessLogic: Confirm Save, return new user ID
BusinessLogic -->> API: Return Respons (Without password)
API -->> A1: Return Message (Success or Failed)
```

**Description**: User sends registration data → API → Service → Repository → Confirmation response.

---

### 2. Place Creation
```mermaid
sequenceDiagram
  actor A1 as User
  participant API as Presentation (API)
  participant BusinessLogic
  participant Persistence as Persistence (Database)


A1 ->> API: User Create Place Request <br>(Title, Description, Price, Latitude, Longitude)
Note over API: Validate and Process Request 
API ->> BusinessLogic: Forward Create_Place Request 
Note over BusinessLogic: Associate Current User as Owner,<br> Generate UUID, Set Create Time
BusinessLogic ->> Persistence: Save Place data (ID, Owner_id, title, discription,<br> price, latitude, longitude, created_at, update_at)
Persistence -->> BusinessLogic: Confirm Save, return new place ID
BusinessLogic -->> API: Return Review object
API -->> A1: Return Message + JSON
```

**Description**: User submits place info → API → PlaceService → DB → response
---

### 3. Review Submission

```mermaid
 sequenceDiagram
  actor A1 as User
  participant API as Presentation (API)
  participant BusinessLogic
  participant Persistence as Persistence (Database)


A1 ->> API: User Review Request (Place_id, rating, comment)
Note over API: Validate and Process Request 
API ->> BusinessLogic: Forward create_Review Request 
Note over BusinessLogic: Validate Rating (1-5),<br>Generate UUID, Create Time
BusinessLogic ->> Persistence: Save Review data (user_id, place_id, rating, comment, created_at, updated_at)
Persistence -->> BusinessLogic: Return review ID and confirmation
BusinessLogic -->> API: Return Review Info
API -->> A1: Return Message (Review Published)
```

**Description**: Validating and saving a user's review for a specific place, ensuring rating bounds (1-5) are respected.

---

### 4. Fetching a List of Places

```mermaid
sequenceDiagram
  actor A1 as User
  participant API as Presentation (API)
  participant BusinessLogic
  participant Persistence as Persistence (Database)

A1 ->> API: User Fetch Places Request
Note over API: Validate and Process Request 
API ->> BusinessLogic: Forward Fetch_Places Request 
Note over BusinessLogic: Process business rules,<br> Prepare database query
BusinessLogic ->> Persistence: Fetch Places data
Persistence -->> BusinessLogic: Return list of Place records <br>(ID, title, price, latitude, longitude, etc.)
BusinessLogic -->> API: Return List of Place objects
API -->> A1: Return Message + JSON Array
```

***Description**: User asks for places → filters applied → DB queried → results returnded

---

## ✅ Final Notes

This document contains all the necessary to start building the HBnB project:
* **The Package Diagram:** Shows the big picture of the system.
* **The Class Diagram:** Shows the database models and their relationships.
* **The Sequence Diagrams:** Show how the system handles user requests step-by-step.

This file should be kept updated as the project grows and new features are added!
