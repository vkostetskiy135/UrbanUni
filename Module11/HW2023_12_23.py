import requests
#requests предоставляет простой и понятный синтаксис для отправки HTTP-запросов и обработки ответов.
#Библиотека поддерживает аутентификацию, работу с куки, загрузку и отправку файлов, а также многие другие функции.
#requests автоматически обрабатывает такие вещи, как кодировка, декомпрессия и управление сессиями,
#что делает её использование более удобным и эффективным по сравнению с базовыми методами Python.
url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print(f"Подводка: {joke['setup']}")
    print(f"Панч: {joke['punchline']}")
else:
    print("Ошибка при получении данных")
