#Задача 1
def func_factory(operation):
    if operation == 'add':
        def add(a, b):
            return a + b
        return add
    elif operation == 'subtract':
        def subtract(a, b):
            return a - b
        return subtract
    elif operation == 'multiply':
        def multiply(a, b):
            return a * b
        return multiply
    elif operation == 'devide':
        def devide(a, b):
            return a / b
        return devide
    elif operation == 'square':
        def square(a, b):
            return a ** b
        return square


func1 = func_factory('add')
print(func1(2, 2))
func1 = func_factory('subtract')
print(func1(5, 3))
func1 = func_factory('multiply')
print(func1(3, 7))
func1 = func_factory('devide')
print(func1(6, 2))
func1 = func_factory('square')
print(func1(2, 3))

#Задача 2
some_func = lambda x: x * 2


def some_same_func(x):
    return x * 2


example = 'Hello world!\n'
print(some_func(example))
print(some_same_func(example))


#Задача 3
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        return self.a * self.b

rect = Rect(5, 5)
print(rect())