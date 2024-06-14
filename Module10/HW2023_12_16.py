from threading import Thread
import queue
import time


class Table:
    def __init__(self, number, busy=False):
        self.number = number
        self.busy = busy
        pass

    def __bool__(self):
        return self.busy


class Customer(Thread):
    def __init__(self, at_table, customer_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.at_table = at_table
        self.customer_num = customer_num

    def run(self):
        self.at_table.busy = True
        time.sleep(5)
        print(f'Посетитель {self.customer_num} покушал и ушел', flush=True)
        self.at_table.busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        def customers():
            for n in range(1, 21):
                print(f'Посетитель номер {n} прибыл', flush=True)
                if all(self.tables):
                    print(f'Посетитель номер {n} ожидает свободный стол', flush=True)
                self.queue.put(n)
                time.sleep(1)

        q = Thread(target=customers)
        q.start()
        serve_thread = Thread(target=self.serve_customer)
        serve_thread.start()
        serve_thread.join()

    def serve_customer(self):
        while True:
            try:
                customer_num = self.queue.get(timeout=1.5)
            except queue.Empty:
                break
            else:
                customer_allocated = False
                while not customer_allocated:

                    for table in self.tables:
                        if not table:
                            print(f'Посетитель номер {customer_num} сел за стол {table.number}', flush=True)
                            Customer(table, customer_num).start()
                            customer_allocated = True
                            break



# # Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
#
# # Инициализируем кафе
cafe = Cafe(tables)



# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

#Вывод :
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 5 прибыл
# Посетитель номер 5 ожидает свободный стол
# ......
# Посетитель номер 20 прибыл
# Посетитель номер 20 ожидает свободный стол
# Посетитель номер 17 покушал и ушёл.
# Посетитель номер 20 сел за стол N.
# Посетитель номер 18 покушал и ушёл.
# Посетитель номер 19 покушал и ушёл.
# Посетитель номер 20 покушал и ушёл.