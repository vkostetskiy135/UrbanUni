class House:
    def __init__(self):
        self.numberOfFloors = 0

    def __str__(self):
        return f'''Number of floors -> {self.numberOfFloors}'''
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors


house = House()
print(house)
house.setNewNumberOfFloors(5)
print(house)