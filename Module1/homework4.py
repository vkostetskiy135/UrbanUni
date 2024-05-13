immutable_var = (True, 'Тру', 1)
print(immutable_var)

#immutable_var[0] = False
#Не сработает потому, как кортеж относится к неизменяемому типу данных и воспринимается как цельный объект

mutable_list = [True, 'Тру', 1, [x for x in range(1, 6)]]
mutable_list[0] = False
print(mutable_list)