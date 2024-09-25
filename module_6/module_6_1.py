class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            return f'{self.name} съела {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стала есть {food.name}'


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


# Создание экземпляров
apatosaurus = Mammal('Long neck')
velociraptor = Predator('Blue')

daisy = Flower('Mayweed')
orange = Fruit('Clockwork Orange')

# Проверка значений
print(apatosaurus.name)
print(velociraptor.name)
print(daisy.name)
print(orange.name)

print(apatosaurus.alive)
print(velociraptor.fed)

# Выполнение методов
print(apatosaurus.eat(orange))
print(velociraptor.eat(daisy))

# Проверка значений после еды
print(apatosaurus.alive)
print(velociraptor.fed)
