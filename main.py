from http.client import HTTPException
from telnetlib import STATUS
from typing import List
from uuid import UUID
from fastapi import FastAPI
from models import Role, User, Gender, UserUpdateRequest

app = FastAPI()

db: List[User] = [User(
    id= UUID("21cb4f27-d24e-4a34-8f6b-3343a37e5314"), 
    first_name="Jonathan",
    last_name="Arias", 
    gender=Gender.male, 
    roles=[Role.admnin]
    ),
    User(
    id=UUID("327a2b9a-7731-4ed5-8493-fc8cd5532825"), 
    first_name="Marcela",
    last_name="Torres", 
    gender=Gender.female, 
    roles=[Role.student]
    )
]

@app.get("/")
async def root():
    return{"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return{"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
   for user in db:
    if user.id == user_id:
        db.remove(user)
    return 
   raise HTTPException(
    status_code=404,
    detail=f"user whit id:{user_id} does not exists")

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
   for user in db:
    if user.id == user_id:
        if user_update.first_name is not None:
            user.first_name = user_update.first_name
        if user_update.last_name is not None:
            user.last_name = user_update.last_name
        if user_update.middle_name is not None:
            user.middle_name = user_update.middle_name
        if user_update.roles is not None:
            user.roles = user_update.roles
    return 
   raise HTTPException(
    status_code=404,
    detail=f"user whit id:{user_id} does not exists")
   