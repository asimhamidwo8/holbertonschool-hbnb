# HBnB API

A Flask + Flask-RESTx REST API for the HBnB (Holberton HBNB; AirBnB recreation)
project. It exposes CRUD-style endpoints for `Users`, `Places`,
`Reviews`, and `Amenities`, built on a three-layer architecture
(Presentation → Business Logic → Persistence) connected through a
Facade, as specified in  `Project Setup and Package Initialization`.

This README documents the project **as it stands today** — the
structure was scaffolded in Task 0 and then filled in incrementally
through Tasks 0–6 (see [Project History](#project-history) below).

## Project Structure

```text
hbnb/
├── app/
│   ├── __init__.py            # Flask app factory: create_app()
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py       # /api/v1/users      endpoints
│   │       ├── places.py      # /api/v1/places     endpoints
│   │       ├── reviews.py     # /api/v1/reviews    endpoints
│   │       └── amenities.py   # /api/v1/amenities  endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py      # Shared id/timestamps + atomic update()
│   │   ├── user.py            # User entity + validation
│   │   ├── place.py           # Place entity + validation
│   │   ├── review.py          # Review entity + validation
│   │   └── amenity.py         # Amenity entity + validation
│   ├── services/
│   │   ├── __init__.py        # Instantiates the HBnBFacade singleton
│   │   └── facade.py          # HBnBFacade: the only door between API and models/storage
│   └── persistence/
│       ├── __init__.py
│       └── repository.py      # Repository ABC + InMemoryRepository
├── tests/
│   ├── __init__.py
│   ├── helpers.py             # Shared fixtures (unique users/places/etc.)
│   ├── test_users.py
│   ├── test_places.py
│   ├── test_reviews.py
│   ├── test_amenities.py
│   └── test_base_model.py
├── run.py                     # Entry point: python run.py
├── config.py                  # Config / DevelopmentConfig
├── requirements.txt           # flask, flask-restx
├── TESTING.md                 # Manual cURL log + automated test report (Task 6)
└── README.md                  # This file
```

### Layer-by-layer purpose

- **`app/api/v1/`** — Presentation layer. Each module defines a
  Flask-RESTx `Namespace`, its Swagger input/output models, and the
  `Resource` classes that map HTTP verbs to facade calls. This layer
  never touches storage directly — it only calls `facade.*`.
- **`app/models/`** — Business Logic layer. Every entity extends
  `BaseModel` (UUID `id`, `created_at`/`updated_at`, a generic
  `update()`). Attribute validation (required fields, email format,
  numeric ranges, rating bounds, etc.) lives in property setters here,
  so it's enforced no matter which layer calls into a model.
- **`app/services/facade.py`** — The `HBnBFacade` class is the single
  entry point the API layer uses to reach the business logic and
  persistence layers (the [Facade pattern](https://refactoring.guru/design-patterns/facade)).
  `app/services/__init__.py` instantiates **one** `facade` object at
  import time, which every namespace module imports — a
  [Singleton](https://refactoring.guru/design-patterns/singleton) shared
  for the lifetime of the process.
- **`app/persistence/repository.py`** — Defines the `Repository`
  interface and an `InMemoryRepository` implementation (plain dict
  keyed by `id`). The facade owns one repository per entity
  (`user_repo`, `place_repo`, `review_repo`, `amenity_repo`). This is
  the seam where Part 3's SQLAlchemy-backed repository will be swapped
  in without changing the facade or API layers.
- **`tests/`** — Automated `unittest` suite exercising every endpoint
  through Flask's test client, plus direct model-level tests. See
  [Testing](#testing) below.

## Requirements

- Python 3.9+ (developed/tested with 3.14)
- `pip`
-  flask
- flask-restx

## Installation

```bash
cd part2/hbnb

# optional but recommended: use a virtual environment
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Running the Application

```bash
python run.py
```

The API is served at `http://127.0.0.1:5000/`. Interactive Swagger
documentation (generated automatically by Flask-RESTx from the models
declared in each `api/v1/*.py` file) is available at:

```text
http://127.0.0.1:5000/api/v1/
```

The raw OpenAPI/Swagger spec is at `http://127.0.0.1:5000/swagger.json`.

## API Overview

| Resource | Endpoint | Methods |
|---|---|---|
| Users | `/api/v1/users/` | `GET`, `POST` |
| | `/api/v1/users/<user_id>` | `GET`, `PUT` |
| Places | `/api/v1/places/` | `GET`, `POST` |
| | `/api/v1/places/<place_id>` | `GET`, `PUT` |
| | `/api/v1/places/<place_id>/reviews` | `GET` |
| Reviews | `/api/v1/reviews/` | `GET`, `POST` |
| | `/api/v1/reviews/<review_id>` | `GET`, `PUT`, `DELETE` |
| Amenities | `/api/v1/amenities/` | `GET`, `POST` |
| | `/api/v1/amenities/<amenity_id>` | `GET`, `PUT` |


## Testing

An automated `unittest` suite lives in `tests/` (no extra dependency —
`unittest` is in the standard library). Run it from `part2/hbnb/`:

```bash
python -m unittest discover -s tests -v
```

For the full manual black-box `cURL` testing log, the bugs that testing
uncovered, and how they were fixed, see **[TESTING.md](./TESTING.md)**.

## Project History

The project was implemented with these specifications:

| Task | What it added |
|---|---|
| `Project Setup and Package Initialization` | The project setup and package initialization for the Flask app and the HBNB app. |
| `Implement Core Business Logic Classes` | Implemented the core business logic classes for the `User`, `Amenity`, `Place`, and `Review` models. |
| `Implement the User Endpoints` | Implemented the `User` model and the `users` endpoints (`POST`/`GET`/`PUT`). |
| `Implement the Amenity Endpoints` | Implemented the `Amenity` model and the `amenities` endpoints. |
| `Implement the Place Endpoints` | Implemented the `Place` model (with owner/amenity relationships) and the `places` endpoints. |
| `Implement the Review Endpoints` | Implemented the `Review` model and the `reviews` endpoints, including `DELETE` and `GET /places/<id>/reviews`. |
| `Implement Testing and Validation of the Endpoints` | Added the `tests/` automated suite and `TESTING.md`; testing surfaced and fixed two bugs: `PUT /users/<id>` didn't enforce email uniqueness, and `BaseModel.update()` could partially apply a multi-field update when one field failed validation (now rolled back atomically). |
