class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def got_to_new_floor(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')


humanthill = House('ЖК "Окна-в-окна"', 25)
dream_house = House('Домик в деревне', 2)

humanthill.got_to_new_floor(17)
dream_house.got_to_new_floor(3)
