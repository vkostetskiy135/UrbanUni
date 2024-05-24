class Car:
    price = 1_000_000
    horse_power = 200

    def horse_powers(self):
        return self.horse_power


class Nissan(Car):
    price = 600_000
    horse_power = 250

    def horse_powers(self):
        return f'Has {self.horse_power} horses'

class Kia(Car):
    price = 300_000
    horse_power = 160

    def horse_powers(self):
        return f'Has {self.horse_power} horses'


car1 = Nissan()
print(car1.horse_powers())
print(car1.price)

car2 = Kia()
print(car2.horse_powers())
print(car2.price)