
### - 21.11.24
### - модуль 16.2 ДЗ

### - (ЗАПУСКАШКА) - python -m uvicorn module_16_2_DZ:app  ### - ВАЖНО для виндовс просто python (без цифр)
### - пример оформления запроса в FastAPI ] http://127.0.0.1:8000/id?username=user&age=34 [

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
@app.get('/')                                              ### - запрос
async def welcome() -> dict:                               ### - какие данные должны выйти (-> dict)
    return {"message": "Главная страница"}

@app.get('/user/admin')
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def id(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1')) -> dict:
    return {"message": f"Вы вошли как пользователь №, {user_id}"}

@app.get('/user/{username}/{age}')
async def get_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
               age: int = Path(ge=18, le=120, description="Enter age", example='24')) -> dict:
    return {"message": f"Информация о пользователе. Имя:, \"{username}\", Возраст: {age}."}

