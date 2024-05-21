class Building:
    def __init__(self, numberOfFloors, type):
        self.numberOfFloors = numberOfFloors
        self.buildingType = type

    def __eq__(self, other):
        if self.numberOfFloors == other.numberOfFloors:
            if self.buildingType == other.buildingType:
                return True
        return False


house1 = Building(20, 'Skyscraper')
house2 = Building(20, 'Skyscraper')
house3 = Building(1, 'Hut')

if Building.__eq__(house1, house2):
    print(f'First and second are alike')

if not Building.__eq__(house2, house3):
    print(f'Second and third are different!')