import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = (
            list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        )
        self.filled = False

        if not self.__is_valid_color(*self.__color):
            raise ValueError('Некорректный цвет')

        if not self.__is_valid_sides(*self.__sides):
            raise ValueError('Некорректное количество или значения сторон')

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return (
            isinstance(r, int)
            and isinstance(g, int)
            and isinstance(b, int)
            and 0 <= r < 256
            and 0 <= g < 256
            and 0 <= b < 256
        )

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(
            isinstance(side, int) and side > 0 for side in new_sides
        )

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius**2)

    def set_radius(self, radius):
        if isinstance(radius, (int, float)) and radius > 0:
            self.__radius = radius
            self.set_sides(radius * 2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        if not (
            self.__sides[0] + self.__sides[1] > self.__sides[2]
            and self.__sides[0] + self.__sides[2] > self.__sides[1]
            and self.__sides[1] + self.__sides[2] > self.__sides[0]
        ):
            raise ValueError('Не выполняется неравенство треугольника')

    def get_square(self):
        s = sum(self.__sides) / 2
        return math.sqrt(
            s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2])
        )


class Cube(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if sides:
            self.__sides = [sides[0]] * 12
        else:
            self.__sides = [1] * 12

    def get_volume(self):
        return self.__sides[0] ** 3

    def get_sides(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
