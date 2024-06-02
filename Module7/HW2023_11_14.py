with open('poetry.txt', mode='r') as file:
    print(file.read())

#оператор with автоматические закрывает раннее открытый файл в конце блока с помощью __exit__