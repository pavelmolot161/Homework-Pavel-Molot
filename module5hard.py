import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname           ### - имя пользователя, строка
        self.password = password           ### - в хэшированном виде, число
        self.age = age                     ### - возраст, число

    def change_password(self, new_password):
        # здесь должен быть код для хэширования нового пароля и сохранения его в атрибуте password
        self.password = hash(new_password)

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title                    ### - заголовок, строка
        self.duration = duration              ### - продолжительность, секунды
        self.time_now = 0                     ### - секунда остановки (изначально 0)
        self.adult_mode = adult_mode          ### - ограничение по возрасту, bool (False по умолчанию))

class UrTube:
    def __init__(self):
        self.users = []                   ### - список объектов User
        self.videos = []                  ### - список объектов Video
        self.current_user = None        ### - текущий пользователь, User

    def log_in(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                # return
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result
#
    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        found_video = None
        for video in self.videos:
            if video_title.lower() == video.title.lower():
                found_video = video
                break
        if found_video:
            if found_video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            # print("Просмотр видео:")
            for second in range(found_video.duration):
                print(second + 1, end=' ')
                time.sleep(1)
            print("Конец видео.")

### Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# Добавление видео
ur.add(v1, v2)

##Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

##Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

##Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

##Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')














































