
### - 22.11.24
### - модуль 16.3 ДЗ

### - (ЗАПУСКАШКА) - python -m uvicorn module_16_3_DZ:app  ### - ВАЖНО для виндовс просто python (без цифр)
### - оформление запроса в FastAPI ] http://127.0.0.1:8000/id?username=user&age=34 [


from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')                                                  ### - запрос на пользователя ПО ЕГО НОМЕРУ
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')                                 ### - запрос на СОЗДАНИЕ
async def greate_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
    example='UrbanUser')], age: int = Path(ge=18, le=120, description="Enter age", example='24')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')                        ### - запрос МЕНЯЕМ СТАРОЕ НА НОВОЕ
async def update_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1'),
                      username: str = "string", age: int = 20) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')                                      ### - запрос на УДАЛЕНИЕ
async def delite_user(user_id: int) -> str:
    users.pop(str(user_id))
    return f'The user with the {user_id} number has been deleted.'

