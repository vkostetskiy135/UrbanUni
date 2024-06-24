def introspection_info(obj):
    info = {}

    #Имя объекта
    info['type'] = type(obj).__name__

    #Добавляет в info только атрибуты, исключая методы класса и магические методы
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    #Добавляет в info только методы класса, исключая магические методы и атрибуты
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    #Например если нужно будет увидеть еще и магические методы
    # info['magic'] = [magic for magic in dir(obj) if magic.startswith('__')]

    #Добавляет в info имя модуля, в котором находится obj
    info['module'] = obj.__module__

    #Если у объекта есть документация, добавляет в info
    if hasattr(obj, '__doc__'):
        info['doc'] = obj.__doc__
    return info


# Example usage
class ExampleClass:
    """Класс для примера"""

    def __init__(self, value):
        self.value = value

    def example_method(self):
        return self.value


example_obj = ExampleClass(10)
print(introspection_info(example_obj))
