


import os
import time

print(os.getcwd())
directory = r'D:\Project(HomeWork)\home work'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        last_modified = os.path.getmtime(filepath)
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        # Преобразуем время последнего изменения в читаемый формат
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified))

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')

        # Выводим информацию о файлe для проверки
        # print(f'Файл: {file}')
        # print(f'Путь: {full_path}')
        # print(f'Время последнего изменения: {last_modified_time}')
        # print(f'Размер файла: {file_size} байт')
        # print(f'Родительская директория: {parent_dir}')
        # print()




















### Давайте разберем, что делает этот код:

# Мы используем os.walk() для обхода директории, указанной в переменной directory. Этот метод возвращает три значения: root (текущая директория), dirs (список поддиректорий) и files (список файлов).
# Для каждого файла мы получаем полный путь с помощью os.path.join().
# Используем os.path.getmtime() для получения времени последнего изменения файла, которое мы затем преобразуем в читаемый формат с помощью time.strftime().
# Получаем размер файла с помощью os.path.getsize().
# Используем os.path.dirname() для получения родительской директории файла.
# Выводим всю собранную информацию о файле.
# Этот код позволит Вам обойти указанную директорию, получить информацию о каждом файле и вывести ее в консоль. Вы можете модифицировать код, чтобы сохранять эту информацию в другом формате, например, в CSV-файл или базу данных, в зависимости от Ваших потребностей.