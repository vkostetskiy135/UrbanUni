from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if self.users[login].password == hash(password):
            self.current_user = self.users[login]
            print('Вы успешно вошли в аккаунт!')
        else:
            print('Ошибка вводе логина или пароля, либо такого пользователя не существует!')
            return


    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
            return
        user = User(nickname, password, age)
        self.users[user.nickname] = user
        self.current_user = user

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')


    def add(self, *args):
        for v in args:
            self.videos.append(v)
        print(f'Добавленные видео:')
        for i, v in enumerate(self.videos, start=1):
            print(f'{i}. - {v.title}\n')

    def get_videos(self, request):
        result = []
        for v in self.videos:
            for i in range(len(v.title)):
                if request.lower() == v.title[i:i + len(request)].lower():
                    result.append(v.title)
                    break
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
            return
        for v in self.videos:
            if v.title == title:
                if v.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    for t in range(1, v.duration + 1):
                        print(t)
                        v.time_now = t
                        sleep(1)
                    print('Конец видео')
                    return
        print('Видео с таким названием не существует!')
        return





class Video:
    '''
    Класс видео, содержит в себе название видео, контент в формате str

    '''
    def __init__(self, title, duration, adult_mode=False):
        #Название
        self.title = title
        #Продолжительность видео в секундах
        self.duration = duration
        #Секунда остановки
        self.time_now = 0
        #Ограничение по возрасту
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
ur.log_in('vasya_pupkin', 'lolkekcheburek')
