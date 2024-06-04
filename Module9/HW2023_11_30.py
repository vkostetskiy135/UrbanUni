some_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
print(list(filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, some_list))))