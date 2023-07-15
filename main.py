from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Role, User

app = FastAPI()

db: List[User] = [
    User(
        id = uuid4(),
        first_name= "Steve",
        last_name="Smith",
        role=[Role.admin]
    ),
    User(
        id = uuid4(),
        first_name= "Kane",
        last_name="Williamson",
        role=[Role.contributor, Role.user]
    ),
    User(
        id = uuid4(),
        first_name= "Joe",
        last_name="Root",
        role=[Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} not found"
    )