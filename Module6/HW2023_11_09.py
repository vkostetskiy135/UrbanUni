import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__sides = None
        self.set_sides(*sides)
        self.__color = None
        self.set_color([x for x in color])
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        for i in color:
            if not isinstance(i, int) or not 0 <= i <= 250:
                return False
        return True

    def set_color(self, color):
        if self.__is_valid_color(color):
            self.__color = color
        else:
            print('Invalid color!')

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            return True
        return False

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = [x for x in args]
            return
        self.__sides = [1 for _ in range(self.sides_count)]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__radius = round(self.get_sides()[0] / (2 * math.pi), 2)

    def get_square(self):
        return round(math.pi * (self.__radius**2), 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__height = self.calculate_heights_or_just_square()

    def get_square(self):
        return self.calculate_heights_or_just_square(square_bool=True)

    #Высота может идти от каждой вершины треугольника, поэтому просто выведу список всех высот
    #И что бы не копировать содержимое этой функции в get_square(), добавил параметр, который в истинном состоянии
    # вернёт только площадь
    def calculate_heights_or_just_square(self, square_bool=False):
        result = []
        names = ['a', 'b', 'c']
        d = dict(zip(names, self.get_sides()))
        half_square = (d['a'] + d['b'] + d['c']) / 2
        square = math.sqrt(half_square * (half_square - d['a']) * (half_square - d['b']) * (half_square - d['c']))
        if square_bool:
            return square
        for v in d:
            result.append(round((2 * square) / d[v], 2))
        return result

    def get_heights(self):
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def set_sides(self, *args):
        if len(args) == 1:
            self.__sides = [args[0] for _ in range(self.sides_count)]
        elif self.__sides is None:
            self.__sides = [1 for _ in range(self.sides_count)]


    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10, 15) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides())