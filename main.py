from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Roles, UpdateUser, User

app = FastAPI()


# demo db
db = User = [
    User(
        id=UUID("02142f55-cbc4-4f5c-b987-896b5b021cd6"),
        first_name='John',
        last_name='Doe',
        middle_name='FastAPI',
        gender=Gender.male,
        roles=[Roles.user]
    ),
    User(
        id=UUID("288583cd-d08d-4260-b95c-14e7df017308"),
        first_name='Mascot',
        last_name='Lane',
        gender=Gender.female,
        roles=[Roles.student, Roles.admin]
    )
]

@app.get('/')
async def root():
    return {'Hello'} 

# To get all the users in the database
@app.get("/api/v1/users")
async def get_users():
    users = db
    return users

# create user
@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {user.id}

# Delete User
@app.delete("/api/v1/users/{user_id}", status_code=204)
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user_id} does not exist'
    )

# Update User
@app.patch("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UpdateUser):
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
            del user.id
            return user
        raise HTTPException(
            status_code=422,
            detail= f'user id: {user_id} is not a valid uuid'
        )
    raise HTTPException(
        status_code = 404,
        detail = f'user with id: {user_id} does not exist'
    )