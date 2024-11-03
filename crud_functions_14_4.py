import asyncio
### - 03.11.24
import sqlite3
import cursor


async def initiate_db():

    connection = sqlite3.connect('database_14_4a.db') ### - создаёт объект соединения (`connection`).
                ## Аргумент `'database.db'` указывает имя файла базы данных.  Если файл `database.db` не существует,
                # он будет создан.  Если он существует, то к нему будет установлено соединение.  Важно отметить,
                # что база данных хранится в файле `database.db` в той же директории, где запущен скрипт.

    cursor = connection.cursor()    ### - Эта строка создаёт курсор.  Курсор — это объект, который позволяет
                            ## выполнять SQL-запросы к базе данных.  Он является интерфейсом для отправки запросов и
                            # получения результатов.  Метод `connection.cursor()` возвращает объект курсора, связанный
                            # с объектом соединения.

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


    connection.commit()  ### - `connection.commit()`** эта строка сохраняет изменения в базе данных. Все изменения,
        ## сделанные с помощью курсора, хранятся в памяти до тех пор, пока не будет вызван метод `commit()`.
        # После выполнения `commit()` изменения записываются в файл базы данных `database.db`.  Если бы эта строка
        # отсутствовала, изменения были бы потеряны после закрытия соединения.
    return connection  # Возвращаем соединение

async def get_all_products(connection):
    cursor = connection.cursor()            ### - Создаём курсор внутри функции
    cursor.execute('SELECT * FROM Products')
    results = cursor.fetchall()             ### - Получаем все результаты запроса
    for row in results:
        print(row)                          ### - Выводим каждую строку
        # return row
    connection.close()                      ### - Закрываем соединение
connection = initiate_db()                  ### - Получаем соединение
connection.close()

#____________________________________________________________________________________________________________

# async def main():                                 ### - <<< включять только при создании таблици
#     connection = await initiate_db()
#     await get_all_products(connection)
# asyncio.run(main())
