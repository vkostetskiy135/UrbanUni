from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, skill, n_enemies=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.n_enemies = n_enemies


    def run(self):
        flush_for_print = True
        print(f'{self.name}, на нас напали!', flush=flush_for_print)
        days_count = 0
        #В случае если например skill рыцаря не кратен n_enemies и число получится отрицательным, вернёт 0
        def not_less_than_zero(n):
            if n < 0:
                return 0
            return n

        while self.n_enemies > 0:
            self.n_enemies -= self.skill
            days_count += 1
            time.sleep(1)
            print(f'{self.name}, сражается {days_count} день(дня)..., осталось {not_less_than_zero(self.n_enemies)} воинов.', flush=flush_for_print)
        print(f'{self.name} одержал победу спустя {days_count} дней!', flush=flush_for_print)


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
time.sleep(0.3)
knight2.start()
knight1.join()
knight2.join()

print('Все битвы закончились!')






