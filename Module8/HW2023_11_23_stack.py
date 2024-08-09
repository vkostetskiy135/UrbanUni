def personal_sim(numbers):
    result = 0
    incorrect_data = 0
    for n in numbers:
        try: result += n
        except TypeError:
            incorrect_data += 1
        print(f'Некорректный тип данных для подсчёта суммы - {n}')
    return (result, incorrect_data)


def calculate_average(*numbers):
    try:
        ps = personal_sim(numbers[0])
    except TypeError:
        print('В numbers записан корректный тип данных')
        return None
    try:
        return ps[0] / (len(numbers[0]) - ps[1])
    except ZeroDivisionError: return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать