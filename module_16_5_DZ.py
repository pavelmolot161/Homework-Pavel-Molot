
### - 25.11.24
### - модуль 16.5 ДЗ (Jinja)

### - (ЗАПУСКАШКА) - python -m uvicorn module_16_5_DZ:app  ### - ВАЖНО для виндовс просто python (без цифр)
### - оформление запроса в FastAPI ] http://127.0.0.1:8000/id?username=user&age=34 [

from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form                    ### - Request - запрос
from fastapi.responses import HTMLResponse                                                   ### - HTMLResponse - ответ
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

                    ### - Используем словарь для хранения пользователей, где ключ - это id пользователя
users_dict = {}                                                        ### - все дело в словаре
class User(BaseModel):
    id: int
    username: str = "Platon"
    age: int = 18

@app.get('/')                                                     ### - Запрос на получение всех пользователей
def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {'request': request, 'users_dict': users_dict})

@app.get(path='/user/{user_id}')                                  ### - Запрос на получение пользователя по id
def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {'request': request, 'user': users_dict[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found (<01>)")

@app.post('/user/{username}/{age}', status_code=status.HTTP_201_CREATED)
def create_user(
        request: Request,
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: int = Path(gt=18, lt=120, description="Enter age", example=24),
        user_str: str = Form()
) -> HTMLResponse:
    try:
        if users_dict:                                     ### - Проверка, содержит ли словарь какие-либо элементы
            user_id = max(users_dict.keys()) + 1
        else:
            user_id = 1                                        ### - Если словарь пуст, ID = 1
        user = User(id=user_id, username=username, age=age)    ### - Создание объекта пользователя

        if username in users_dict:                         ### - Проверка на существование пользователя с таким именем
            raise HTTPException(status_code=400, detail="Username already exists (<02>).")
        users_dict[user_id] = user                              ### - Добавляем пользователя в словарь
        return templates.TemplateResponse("users.html", {'request': request, 'users_dict': users_dict})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found (<03>).")

@app.put('/user/{user_id}/{username}/{age}')                                ### - Запрос на обновление пользователя
def update_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1'),
                      username: str = "string", age: int = 20) -> str:
    if user_id not in users_dict:
        raise HTTPException(status_code=404, detail="User was not found (<04>).")
    user = User(id=user_id, username=username, age=age)
    users_dict[user_id] = user                                              ### - Обновляем пользователя в словаре
    return f"The user {user_id} is updated (<05>)."

@app.delete('/user/{user_id}')                                              ### - Запрос на удаление пользователя
def delete_user(user_id: int) -> str:
    if user_id in users_dict:
        del users_dict[user_id]                                             ### - Удаляем пользователя из словаря
        return f'The user with the id {user_id} has been deleted (<06>).'
    else:
        raise HTTPException(status_code=404, detail="User was not found (<07>).")








