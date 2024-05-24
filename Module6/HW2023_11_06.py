class Vehicle:
    def __init__(self):
        self.vehicle_type = None


class Car:
    horse_power = 200

    def __init__(self):
        self.price = 1_000_000

    def horse_powers(self):
        return self.horse_power


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 300_000
        self.vehicle_type = str(self.__class__.__name__)

    horse_power = 300

    def __str__(self):
        return f'{self.vehicle_type} has {self.horse_power} horses just for {self.price}!'


car1 = Nissan()
print(car1)
