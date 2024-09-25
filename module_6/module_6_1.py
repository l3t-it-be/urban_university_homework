class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            self.fed = True
            return f'{self.name} съела {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стала есть {food.name}'


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            self.fed = True
            return f'{self.name} съела {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стала есть {food.name}'


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


apatosaurus = Mammal('Long neck')
velociraptor = Predator('Blue')

daisy = Flower('Mayweed')
orange = Fruit('Clockwork Orange')

print(apatosaurus.name)
print(velociraptor.name)
print(daisy.name)
print(orange.name)

print(apatosaurus.alive)
print(velociraptor.fed)

print(apatosaurus.eat(orange))
print(velociraptor.eat(daisy))

print(apatosaurus.alive)
print(velociraptor.fed)
