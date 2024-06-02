# with open('poetry.txt', mode='r') as file:
#     print(file.read())

file = open('poetry.txt', mode='r')
file_content = file.read()
print(file_content)
file.close()