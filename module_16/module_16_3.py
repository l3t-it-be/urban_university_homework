from typing import Annotated
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def register_user(
    username: Annotated[
        str,
        Path(
            min_length=4,
            max_length=20,
            description='Enter username',
            examples=['UrbanUser'],
        ),
    ],
    age: Annotated[
        int, Path(ge=18, le=65, description='Enter age', examples=[24])
    ],
) -> str:
    if users:
        user_id = str(int(max(users, key=int)) + 1)
    else:
        user_id = '1'
    user = f'Имя: {username}, возраст: {age}'
    users[user_id] = user
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[
        str,
        Path(
            min_length=1,
            max_length=3,
            description='Enter User ID',
            examples=['1'],
        ),
    ],
    username: Annotated[
        str,
        Path(
            min_length=4,
            max_length=20,
            description='Enter username',
            examples=['UrbanUser'],
        ),
    ],
    age: Annotated[
        int, Path(ge=18, le=65, description='Enter age', examples=[25])
    ],
) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    user = f'Имя: {username}, возраст: {age}'
    users[user_id] = user
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(
    user_id: Annotated[
        str,
        Path(
            min_length=1,
            max_length=3,
            description='Enter User ID',
            examples=['1'],
        ),
    ]
) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    del users[user_id]
    return f'User {user_id} has been deleted'


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost')
