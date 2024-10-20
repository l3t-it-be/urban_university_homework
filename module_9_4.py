from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

same_letters = list(map(lambda x, y: x == y, first, second))

result = same_letters
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data}\n')

    return write_everything


write = get_advanced_writer('module_9/example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def call(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball.call())
print(first_ball.call())
print(first_ball.call())
