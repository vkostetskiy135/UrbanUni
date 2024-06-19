from multiprocessing import Process, Lock
from collections import defaultdict

class WarehouseManager(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = defaultdict(int)
        pass

    #Функции self.receipt и self.shipment по факту отличаются только одним знаком
    #По-хорошему объединить в одну, но этого требует ТЗ
    def receipt(self, request):
        product, quantity = request[0], request[2]
        self.data[product] += quantity

    def shipment(self, request):
        product, quantity = request[0], request[2]
        self.data[product] -= quantity

    # Функция сортировщик, тоже не вижу надобности для неё существовать отдельно. Можно было вставить в self.run()
    def process_request(self, request: tuple):
        if request[1] == 'receipt':
            self.receipt(request)
        elif request[1] == 'shipment':
            self.shipment(request)

    def run(self, requests):
        for request in requests:
            self.process_request(request)

        print('Data modified:')
        for key, item in self.data.items():
            print(f'{key} : {item}')


    #Как по мне, self.run() должен выглядеть вот так. В два раза короче, но не менее читабельный.

    # def run(self, requests: list):
    #     for request in requests:
    #         product, action, quantity = request
    #         if action == 'receipt':
    #             self.data[product] += quantity
    #         elif action == 'shipment':
    #             self.data[product] -= quantity
    #
    #     print('Data modified:')
    #     for key, item in self.data.items():
    #         print(f'{key} : {item}')





# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)