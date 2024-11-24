
### - 24.11.24
### - модуль 16.4 ДЗ

### - (ЗАПУСКАШКА) - python -m uvicorn module_16_4_DZ:app  ### - ВАЖНО для виндовс просто python (без цифр)
### - оформление запроса в FastAPI ] http://127.0.0.1:8000/id?username=user&age=34 [


from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

                    ### - Используем словарь для хранения пользователей, где ключ - это id пользователя
users_dict = {}                                                        ### - все дело в словаре


class User(BaseModel):
    id: int
    username: str = "Platon"
    age: int = 18

@app.get('/users')                                                     ### - Запрос на получение всех пользователей
async def get_users() -> List[User]:
    return list(users_dict.values())

@app.post('/user/{username}/{age}')                                        ### - Запрос на создание пользователя
def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                              example='UrbanUser')],
                age: int = Path(ge=18, le=120, description="Enter age", example='24')) -> str:
    try:

##########_________________ИЗМЕНЕНИЯ __________________________________________

        if users_dict:                            ### - проверка содержит ли словарь какие либо элементы
            user_id = max(users_dict.keys()) + 1  ### - Если словарь не пуст, мы используем функцию max(), чтобы найти
                                                   ## максимальный ключ к которому добавляем 1, чтобы
                                                    # получить новый уникальный идентификатор (user_id)
                                                    # для следующего пользователя.
        else:
            user_id = 1                           ### - если словарь пуст то id = 1

##########_____________________________________________________________________

        user = User(id=user_id, username=username, age=age)
        users_dict[user_id] = user                                         ### - Добавляем пользователя в словарь
        return f"User {user} is registered (<01>)"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found (<02>).")

@app.put('/user/{user_id}/{username}/{age}')                               ### - Запрос на обновление пользователя
async def update_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1'),
                      username: str = "string", age: int = 20) -> str:
    if user_id not in users_dict:
        raise HTTPException(status_code=404, detail="User was not found (<03>).")

    user = User(id=user_id, username=username, age=age)
    users_dict[user_id] = user                                              ### - Обновляем пользователя в словаре
    return f"The user {user_id} is updated (<04>)."


@app.delete('/user/{user_id}')                                              ### - Запрос на удаление пользователя
async def delete_user(user_id: int) -> str:
    if user_id in users_dict:
        del users_dict[user_id]                                             ### - Удаляем пользователя из словаря
        return f'The user with the id {user_id} has been deleted (<05>).'
    else:
        raise HTTPException(status_code=404, detail="User was not found (<06>).")





