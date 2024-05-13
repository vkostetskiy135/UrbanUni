my_list = ['Orange', 'Apple', 'Banana', 'Peach', 'Pineapple']
print(f'List: {my_list}')
print(f'First element: {my_list[0]}\nLast element: {my_list[-1]}')
print(f'Sublist: {my_list[2:5]}')
my_list[2] = 'Coconut'
print(f'Modified list : {my_list}')

my_dict = {'Апельсин': my_list[0], 'Яблоко': my_list[1], 'Кокос': my_list[2]}
print(f"Dictionary : {my_dict}")
print(f'Translation: {my_dict["Кокос"]}')
my_dict['Банан'] = 'Banana'
print(f'Modified dictionary : {my_dict}')