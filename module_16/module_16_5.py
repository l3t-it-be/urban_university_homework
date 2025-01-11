from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse, summary='Get Main Page')
async def get_users(request: Request):
    return templates.TemplateResponse(
        'users.html', {'request': request, 'users': users}
    )


@app.get('/user/{user_id}', response_class=HTMLResponse, summary='Get User')
async def get_user(request: Request, user_id: int):
    try:
        user = users[user_id - 1]
        return templates.TemplateResponse(
            'users.html', {'request': request, 'user': user}
        )
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/{username}/{age}', summary='Post User')
async def register_user(username: str, age: int) -> str:
    user = User(username=username, age=age)
    user.id = len(users) + 1
    users.append(user)
    return f'User {user.id} is registered'


@app.put('/user/{user_id}/{username}/{age}', summary='Update User')
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}', summary='Delete User')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id - 1)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost')
