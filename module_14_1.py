
import random
import sqlite3

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

'''СОЗДАНИЕ БАЗЫ ДАННЫХ'''

# for i in range(10):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f"User{i}",
#                     f"{i}ex@gmail.com", str(random.randint(10, 61)), 1000))                ### - (+)

'''ВНЕСЕНИЕ ИЗМЕНЕНИЙ В БАЗУ ДАННЫХ'''
# for i in range(0, 10, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))   ### - (+)

'''УДАЛЕНИЕ ПАРАМЕТРОВ ИЗ БАЗЫ ДАННЫХ'''
# for i in range(0, 10, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?',(f'User{i}',) )                   ### - (+)

cursor.execute('SELECT * FROM Users')

'''МЕТОДЫ'''
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))   ### - (+)

users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
