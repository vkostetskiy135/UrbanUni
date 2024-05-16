from math import factorial


def test(*args):
    print(*args)


test('Первый', True, 1)


def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


print(factorial_rec(5))


#Но вместо написания рекурсий лучше импортировать из math
print(factorial(5))