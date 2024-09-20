class House:

    houses_history = []

    def __new__(cls, *args):
        house = super().__new__(cls)
        cls.houses_history.append(args[0])
        return house

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


life_park = House('ЖК "Life Park"', 18)
print(House.houses_history)
sunny = House('ЖК "Солнечный"', 9)
print(House.houses_history)
apricot = House('ЖК "Абрикос"', 15)
print(House.houses_history)

del life_park
del apricot

print(House.houses_history)
