# Food Tracker Backend API

Production-ready starter backend API for tracking foods, logging meals, and monitoring daily macro goals.

## Features
- JWT authentication (`/auth/register`, `/auth/login`)
- User profile + nutrition goal management
- Food catalog CRUD-lite (create/list/get)
- Food entry logging by day + meal type
- Daily nutrition summary with calorie/protein/carbs/fat totals vs goals
- SQLite persistence with SQLAlchemy ORM
- OpenAPI docs via FastAPI (`/docs`)

## Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API runs at `http://127.0.0.1:8000`.

## Core Endpoints
### Auth
- `POST /auth/register`
- `POST /auth/login`

### User
- `GET /users/me`
- `PUT /users/me/goals`

### Foods
- `POST /foods`
- `GET /foods`
- `GET /foods/{food_id}`

### Entries
- `POST /entries`
- `GET /entries?consumed_date=YYYY-MM-DD`
- `GET /entries/daily-summary?consumed_date=YYYY-MM-DD`

## Testing
```bash
pytest
```
