
### - 21.11.24
### - модуль 16.1 ДЗ
# from uvicorn
### (ЗАПУСКАШКА) - python -m uvicorn module_16_1_DZ:app    ### - ВАЖНО для виндовс просто python

from fastapi import FastAPI

app = FastAPI()
@app.get('/')                                              ### - запрос
async def welcome() -> dict:                               ### - какие данные должны выйти (-> dict)
    return {"message": "Главная страница"}

@app.get('/user/admin')
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def id(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь №, {user_id}"}

@app.get('/user')
async def news(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя:, \"{username}\", Возраст: {age}."}

















