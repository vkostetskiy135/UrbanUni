class Student:

    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    # Раскомментируйте две функции ниже, что бы все тесты провалились
    # def run(self):
    #     self.distance += 5
    #
    # def walk(self):
    #     self.distance += 10

    def __str__(self):
        return self.name

