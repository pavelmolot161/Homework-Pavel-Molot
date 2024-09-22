import multiprocessing
import os
import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()   ### - Метод readline () считывает строку и, также как и с методом read (),
                                       # сдвигает курсор — только теперь уже на целую строку.
                                       # Применение этого метода несколько раз будет приводить к
                                       # считыванию нескольких строк.
            if not line:
                break
            all_data.append(line)

        ### - Линейное считывание:

# files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# start = datetime.datetime.now()
#
# read_info('file 1.txt')
# read_info('file 2.txt')
# read_info('file 3.txt')
# read_info('file 4.txt')
#
# end = datetime.datetime.now()
# print(f'Линейное время выполнения = ({end - start})') ### - Линейное время выполнения = (0:00:09.417321)

        ### - Многопроцессное считывание:

if __name__ == "__main__":                                 ### - Проверка на то что запускаемый файл является основным
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool: ### - Pool принимает количество процессов которые нужно запустить
        start = datetime.datetime.now()
        pool.map(read_info, filenames)   ### - Pool — это класс в модуле multiprocessing в Python,
                                            # который предоставляет пул процессов для выполнения задач параллельно.
                                            # Он позволяет управлять пулом процессов и распределять задачи между ними.
                            # - Pool - принимает первым аргументом функцию которая определяет работу каждого процесса и
                            # вторым аргументом принимае список названий рисунков
                            # ОН ОПРЕДЕЛЯЕТ ПРОГОН ЧЕРЕЗ ФУНКЦИЮ СПИСОК РИСУНКОВ
    end = datetime.datetime.now()
    print(f'Многопроцессное время выполнения = ({end - start})') ### - >>> Многопроцессное время выполнения
                                                                   # = (0:00:04.403995)
