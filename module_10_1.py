
from threading import Thread
from time import sleep
from datetime import datetime
time_start = datetime.now()

def wite_words(word_count, file_name):                  ### - word_count - количество записываемых слов,
                                                        ### - file_name - название файла, куда будут записываться слова.
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):              ### - Внутри цикла for мы проходим по диапазону
                                                        ## от 1 до num_repeats + 1, чтобы пронумеровать каждую строку.
            sleep(0.1)                                  # ??? - пауза в выполнении потока (для чего она нужна - ?)
            file.write(f'Какое-то слово № {i} \n')      ### - {i} - номер итерации в строке
    print(f"Завершилась запись в файл, {file_name} ")

wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

time_end = datetime.now()
time_result = (time_end - time_start)                   ### - расчет времени затраченного на операции
print(f'Работа потоков {time_result}')

time_start_2 = datetime.now()

thread_1 = Thread(target=wite_words, args=(10, "example5.txt"))   ### - Thread(функция, (аргумент, аргумент))
thread_2 = Thread(target=wite_words, args=(30, "example6.txt"))
thread_3 = Thread(target=wite_words, args=(200, "example7.txt"))
thread_4 = Thread(target=wite_words, args=(100, "example8.txt"))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end_2 = datetime.now()
time_result_2 = (time_end_2 - time_start_2)              ### - расчет времени затраченного потоковые операции
print(f'Работа потоков {time_result_2}')

