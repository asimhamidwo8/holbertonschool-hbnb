# HBnB Evolution – Technical Documentation

This document serves as the foundational technical documentation for the HBnB Evolution project. It compiles all architectural diagrams, business logic models, and API interaction flows designed during the initial phase of the project. This guide is intended to help developers and collaborators understand the core system architecture.

---

## 📘 Introduction

**HBnB Evolution** is a simplified, layered backend application inspired by Airbnb. The system is designed to allow users to:
* Register and manage accounts.
* Create and list properties (Places).
* Submit and view reviews for specific places.
* View amenities associated with places.

This documentation presents the full architectural overview, including:
* The High-Level Layered Architecture (Package Diagram).
* The Detailed Class Diagram for the Business Logic Layer.
* Sequence Diagrams illustrating the interaction flow for core API operations.

---

## 🧱 High-Level Architecture – Package Diagram

![High-Level Architecture](link-to-your-image.png)

### Architectural Layers:
1. **Presentation Layer:** Contains the `API` and `Services`. It acts as the entry point for the application, handling incoming client requests.
2. **BusinessLogic Layer:** Contains the core models (`User`, `Place`, `Review`, `Amenity`). It receives requests from the Presentation Layer via the **Facade Pattern**, processes business rules, and ensures data integrity.
3. **Persistence Layer:** Contains the `Database` and `Repository`. It handles data storage, retrieval, and database operations based on commands from the Business Logic Layer.

---

## 🏛️ Detailed Class Diagram

[cite_start]Below is the Detailed Class Diagram representing the Business Logic Layer, including the entities, their attributes, methods, and relationships[cite: 5, 6, 7, 8, 9].

```mermaid
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
