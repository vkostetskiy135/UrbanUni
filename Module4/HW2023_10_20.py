def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()

#Не сработает, потому что функция inner_function существует только локально внутри test_function
# inner_function()