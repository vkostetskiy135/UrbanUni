def custom_write(file_name: str, strings: list):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, 1):
            start_position = file.tell()
            file.write(string + '\n')
            strings_positions[(i, start_position)] = string

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
