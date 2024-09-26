
### 1 - Библиотека requests___________________________________________________________________________________

import requests
from bs4 import BeautifulSoup                                    ### - Библиотека для парсинга HTML и XML документов,
                                                                   # которая помогает извлекать данные из HTML.
def article_title(max_requests):

    news_it = 'https://habr.com/ru/news/'
    request_count = 0
    while request_count < max_requests:
        try:                                        ### - Начинаем блок `try`, чтобы отлавливать возможные исключения,
                                                      # которые могут возникнуть из-за проблем
                                                      # с сетью или неправильным URL.
            r1 = requests.get(news_it)
            if r1.status_code == 200:                           ### - проверка статуса ответа

                soup = BeautifulSoup(r1.text, 'html.parser')          ### - парсим тексты на заголовки
                articles = soup.find_all('article')   ### - Метод .find_all() модуля BeautifulSoup4 просматривает и извлекает
                                                   ## ВСЕХ потомков тега, которые соответствуют переданным фильтрующим
                                                    # аргументам
                                                    # - Ищем все статьи
                for article in articles:
                    title = article.find('h2')       ### - Метод .find() похож на метод .find_all(), но извлекает только
                                                       # первый найденный HTML-тег
                                                     ### - элемент <h2>, обычно используется для заголовков второго уровня.
                    if title:
                        request_count += 1
                        title_text = title.get_text(strip=True) ### - обработка и извлечение заголовка
                        link = title.find('a')['href'] ### - атрибут 'href' найденного элемента 'a', получaet значение ссылки
                        print(f"Заголовок: {title_text}")
                        print(f"Ссылка: {link}\n")
            else:
                break
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
            break

# article_title(2)    ### - <<< ВЫЗОВ ФУНКЦИИ

def request_s(max_requests):
    response1 = requests.get("https://www.google.com") ### - использовать этот подход для получения данных с любого
                                                # веб-сайта, что полезно для:
                                                #   - Извлечения текстовой информации (например, новостей, статей, цен).
                                                #   - Скачивания графики или других файлов.
    print(response1.headers)

    data = {'key1': 'value1', 'key2': 'value2'}
    request_count = 0
    while request_count < max_requests:
        response2 = requests.post("https://httpbin.org/post", data=data)   ### - Используется для:
            # - Отправки данных форм на сервер (например, регистрации, авторизации).
            # - Взаимодействия с API, которые требуют отправлять данные (например, обновление записей в базе данных).

        print(response2.headers)
        request_count += 1

# request_s(2)    ### - <<< ВЫЗОВ ФУНКЦИИ

### 2 - Библиотека pandas___________________________________________________________________________________

import pandas

def sistem_red(output_lines):
    try:
        df = pandas.read_csv('./read_file_11/CSV_file_1.txt') ### - читаем файл CSV_file_1.txt, расположенный в
                                    # директории ./read_file_11/, с помощью функции read_csv.
                                    # Если файл успешно читается, данные сохраняются в переменной df в виде DataFrame.
        print(df.head(output_lines)) ### - используем метод head(), чтобы вывести первые output_lines строк из DataFrame.
    except Exception as evil_mistake:
        print(f"Произошла ошибка в sistem_red: {evil_mistake}")

# sistem_red(20)    ### - <<< ВЫЗОВ ФУНКЦИИ

def unique_word(min_count):
    try:
        df = pandas.read_csv('./read_file_11/CSV_file_1.txt', sep=',')
        print("Столбцы в DataFrame:", df.columns.tolist())
        unique_values = df['Город'].value_counts()
        filtered_values = unique_values[unique_values > min_count]
        return (filtered_values)
    except Exception as evil_mistake:
        print(f"Произошла ошибка в unique_word: {evil_mistake}")

# result_4 = unique_word(10)    ### - <<< ВЫЗОВ ФУНКЦИИ
# print(result_4)

def basic_statistics():
    try:
        df = pandas.read_csv('./read_file_11/random_numb_1.txt', sep=r'\s+') ### - Параметр sep=r'\s+' указывает, что данные разделены пробелами (один или более). r перед строкой делает её сырой, что позволяет правильно интерпретировать \s как регулярное выражение для обозначения пробелов.
        print("Столбцы в DataFrame:", df.columns.tolist()) ### - columns возвращает индекс объектов с названиями столбцов, а метод tolist() преобразует его в обычный список.
        print(df.describe())  ### - describe(), который возвращает статистические характеристики числовых столбцов в DataFrame.
    except Exception as evil_mistake2:
        print(f"Произошла ошибка при чтении файла в basic_statistics: {evil_mistake2}")

# basic_statistics()     ### - <<< ВЫЗОВ ФУНКЦИИ

'''метод describe(), который возвращает статистические характеристики числовых столбцов в DataFrame. Это включает такие параметры, как:
  - count (количество непустых значений)
  - mean (среднее значение)
  - std (стандартное отклонение)
  - min (минимальное значение)
  - max (максимальное значение)
  - 25%, 50%, и 75% квартиль (значения, разделяющие последовательность на четыре равные части).'''

### 3 - Библиотека matplotlib________________________________________________________________________________

import matplotlib.pyplot as plt
import numpy as np

def line_graph(x, y):
    plt.figure(figsize=(8, 5))          ### - figure(), чтобы создать новое окно для графика.
                                        ### - figsize=(8, 5) определяет размер окна графика в дюймах (ширина x высота).
    plt.plot(x, y, marker='o')    ### - plot() из библиотеки matplotlib для построения графика.
                                        ## - x и y — это координаты точки. marker='o' добавляет маркеры (кружочки)
                                        # на линии графика, чтобы выделить конкретные точки.
    plt.title('Линейный график')        ### - Устанавливаем заголовок графика с помощью title().
    plt.xlabel('X-значения')            ### - метод xlabel() для задания метки (названия) оси X. Указываем,
                                        ## что ось X будет представлять "X-значения".
    plt.ylabel('Y-значения')
    plt.grid()                          ### - grid() для отображения сетки на графике.
    plt.show()                          ### - show(), который отображает финальный график.

# line_graph([1, 2, 3, 4, 5], [10, 15, 12, 18, 20])    ### - <<< ВЫЗОВ ФУНКЦИИ

def creating_histogram():
    data = np.random.randn(1000)
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, alpha=0.7, color='blue')   ### - hist() для создания гистограммы.
    plt.title('Гистограмма')
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.grid()
    plt.show()

# creating_histogram()    ### - <<< ВЫЗОВ ФУНКЦИИ

'''         метод - hist() для создания гистограммы.
      - data — массив случайных чисел, которые будут отображены на гистограмме.
      - bins=30 — количество корзин (интервалов), на которые будут разбиты данные. Здесь мы используем 30 корзин для наглядности.
      - alpha=0.7 — уровень прозрачности гистограммы (от 0 до 1), где 1 — полностью непрозрачный, а 0 — полностью прозрачный.
      - color='blue' — установка цвета гистограммы.'''

def pie_chart(sizes, labels, colors):
    plt.figure(figsize=(8, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Круговая диаграмма')
    plt.axis('equal')  ### - plt.axis('equal'), чтобы обеспечить равные пропорции для осей X и Y.
                        ## Это позволяет круговой диаграмме выглядеть как круг, а не как эллипс
    plt.show()
                                                                                    ### - <<< ВЫЗОВ ФУНКЦИИ
# pie_chart([15, 30, 45, 10], ['A', 'B', 'C', 'D'], ['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])

'''  - sizes — список чисел, представляющих размеры сегментов диаграммы.
     - labels — список строк, представляющих метки для каждого сегмента.
     - colors — список цветов для каждого сегмента диаграммы.'''

'''         метод - plt.pie() для создания круговой диаграммы с следующими параметрами:
      - sizes — размеры сегментов, которые основываются на значениях, переданных в функцию.
      - labels — метки, которые будут отображаться рядом с каждым сегментом диаграммы.
      - colors — цвета, используемые для сегментов.
      - autopct='%1.1f%%' — форматирует отображение процентов на каждом сегменте. Здесь %1.1f%% означает, 
      что будет показываться число с одним знаком после запятой, а затем знак процента.
      - startangle=140 — определяет угол начала заполнения круговой диаграммы. Это позволяет поворачивать круговую 
      диаграмму на 140 градусов по часовой стрелке.'''













