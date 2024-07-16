import json


def employees_rewrite(sort_type):

    with open('Employees/employees.json', 'r') as file:
        empl_data = json.load(file)

    #Блок ниже убивает двух зайцев - приводит sort_type к регистру ключей, и проверяет что ключ для сортировки имеется у словаря
    for i, key in enumerate(empl_data['employees'][0], 1):
        if sort_type.lower() == key.lower():
            sort_type = key
            break
        if i == len(empl_data[0][0]):
            raise ValueError('Bad key for sorting')

    result_sorted = sorted(empl_data['employees'], key=lambda x: x[sort_type])

    with open(f'Employees/employees_{sort_type}_sorted.json', 'w') as output:
        json.dump({'employees': result_sorted}, output, indent=4)


employees_rewrite('firstName')