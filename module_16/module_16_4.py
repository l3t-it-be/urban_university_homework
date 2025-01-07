from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def register_user(user: User) -> str:
    user.id = len(users)
    users.append(user)
    return f'User {user.id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run(app, host='localhost')
