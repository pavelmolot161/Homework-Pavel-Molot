

def all_variants(text):
    # len_t = len(text)
    for i in range(1, len(text) + 1):
    ### - Внешний цикл перебирает длины подстрок, начиная от 1 и до длины исходной строки text включительно
        for j in range(len(text) - i + 1):
        ### - Внутренний цикл перебирает возможные стартовые индексы для текущей длины,
        ## - гарантирует, что подстрока не выйдет за пределы строки.
            yield text[j:j + i] 

    ### - Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
    ### - Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
#















