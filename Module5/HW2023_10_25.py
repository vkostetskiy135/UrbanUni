class House:
    def __init__(self):
        self.numberOfFloors = 10

    def go_to_ground_floor(self):
        while self.numberOfFloors != 1:
            print(f'Текущий этаж {self.numberOfFloors}\nСпускаемся\n')
            setattr(self, 'numberOfFloors', self.numberOfFloors - 1)
        print(f'Ура! Мы на {self.numberOfFloors} этаже')


house = House()
print(house.__getattribute__('numberOfFloors'))
print(house.numberOfFloors)
print(getattr(house, 'numberOfFloors'))

house.go_to_ground_floor()