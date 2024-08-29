
import io
def custom_write(file_name, strings):
    strings_positions = {}   ### - +
    number = 1               ### - +
    file = open(file_name, 'w', encoding='utf-8')   ### - r - read (читать), w - write (запись), a - append (добавлять)

    for string in strings:
        strings_positions[(number, file.tell())] = string
        # file.write(string)
        file.write(string + '\n')                          ### - записываем строку с переводом строки
        number += 1
    file.close()                                       ### - закрытие файла

    return strings_positions

### - Пример выполняемого кода:

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

### - Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')