import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')
    return write_everything


# Пример использования
write = get_advanced_writer('example.txt')
write("Это строчка", ['A', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Пример использования
first_ball = MysticBall(['Да', 'Нет', 'Наверное'])

print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())

