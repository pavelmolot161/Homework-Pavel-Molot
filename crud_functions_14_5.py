
### - crud_functions_14_5.py
### - 06.11.24
import asyncio
import sqlite3
import cursor

async def initiate_db():
    connection = sqlite3.connect('database_14_4a.db')
    cursor = connection.cursor()
    #
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ("EVLL 1", "Добавка", "1500"))
    #
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ("MY PROTEIN 2", "Протеин", "3700"))
    #
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ("BCA + 3", "BCA Кислота", "4200"))
    #
    # cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                ("TITANIUM 4", "МЕГА протеин", "6900"))

    # connection.commit()
    # return connection

###________ДЗ_14_5______________________________________________________________________________________________

    connection1 = sqlite3.connect('database_14_5.db') ### - создаёт объект соединения (`connection`).
                ## Аргумент `'database.db'` указывает имя файла базы данных.  Если файл `database.db` не существует,
                # он будет создан.  Если он существует, то к нему будет установлено соединение.  Важно отметить,
                # что база данных хранится в файле `database.db` в той же директории, где запущен скрипт.

    cursor1 = connection1.cursor()    ### - Эта строка создаёт курсор.  Курсор — это объект, который позволяет
                            ## выполнять SQL-запросы к базе данных.  Он является интерфейсом для отправки запросов и
                            # получения результатов.  Метод `connection.cursor()` возвращает объект курсора, связанный
                            # с объектом соединения.

    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email  TEXT NOT NULL,
    reg_age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    connection1.commit()  ### - `connection.commit()`** эта строка сохраняет изменения в базе данных. Все изменения,
        ## сделанные с помощью курсора, хранятся в памяти до тех пор, пока не будет вызван метод `commit()`.
        # После выполнения `commit()` изменения записываются в файл базы данных `database.db`.  Если бы эта строка
        # отсутствовала, изменения были бы потеряны после закрытия соединения.
    return connection1  # Возвращаем соединение

def add_user(username, email, reg_age, balance):
    connection1 = sqlite3.connect('database_14_5.db')
    cursor1 = connection1.cursor()
    check_user = cursor1.execute('SELECT * FROM Users WHERE username = ?', (str(username), ))
                                                                            ### 1 - проверяем есть ли у нас пользователь
    if check_user.fetchone() is None:                                       ### 2 - если пользователя нет (условие)
        cursor1.execute('''                                          
            INSERT INTO Users (username, email, reg_age, balance) 
            VALUES (?, ?, ?, ?)
        ''', (username, email, reg_age, balance))        ### 3 - добавляем пользователя с указанными данными

#         cursor1.execute(f'''
#     INSERT INTO Users VALUES('{username}', '{str(email)}', '{reg_age}', {balance})              ### - НЕ РАБОТАЕТ
# ''')

    connection1.commit()                                              ### 5 - сохраняем изменения в базе данных
    connection1.close()                                               ### - Важно закрывать соединение
def is_included(username):
    connection1 = sqlite3.connect('database_14_5.db')
    cursor1 = connection1.cursor()
    print(type(username))
    check_user = cursor1.execute('SELECT username FROM Users WHERE username = ?', (str(username), )).fetchone()
    connection1.close()                                               ### - Важно закрывать соединение
    return check_user is not None

async def get_all_products():
    connection = sqlite3.connect('database_14_4a.db')
    cursor = connection.cursor()            ### - Создаём курсор внутри функции
    cursor.execute('SELECT * FROM Products')
    results = cursor.fetchall()             ### - Получаем все результаты запроса
    for row in results:
        print(row)                          ### - Выводим каждую строку
        return row
    connection.close()                      ### - Закрываем соединение
connection = initiate_db()                  ### - Получаем соединение
connection.close()

async def get_all_users():
    connection1 = sqlite3.connect('database_14_5.db')
    cursor1 = connection1.cursor()
    cursor1.execute('SELECT * FROM Users')
    results1 = cursor1.fetchall()
    for row1 in results1:
        print(row1)
        return row1
    connection1.close()
connection1 = initiate_db()
connection1.close()

#____________________________________________________________________________________________________________

# async def main():                                 ### - <<< включять только при создании таблици почемуто
#                                                   ## не работает главный файл когда включено
#     await initiate_db()
#     await get_all_products()
# asyncio.run(main())
#
# async def main1():                                 ### - <<< включять только при создании таблици
#     await initiate_db()
#     await get_all_users()
# asyncio.run(main1())