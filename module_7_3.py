
import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for text in self.file_names:                        ### - прошли по, (*args) бесконечному списку с названиями
            with open(text, encoding='utf-8') as file:
                info = file.read().lower()
                for sum in punctuation:
                    info = info.replace(sum,'')
                all_words[self.file_names] = info.split()
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                result[file_name] = words.count(word.lower())
        return result



###    Пример выполнения программы:   ###

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


