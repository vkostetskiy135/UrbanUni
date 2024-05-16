def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, b='не строка', c=False)

#Оба работают, но PyCharm ругается что получает не то, что ожидает
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [1, 'Тру', True]
values_dict = {'a': 1, 'b': 'Тру', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'два']

#Работает
print_params(*values_list_2, 42)

