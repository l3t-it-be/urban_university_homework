import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0
        self.winner = False

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power

            if self.enemies < 0:
                remaining_enemies = 0
            else:
                remaining_enemies = self.enemies

            print(
                f'{self.name} сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.'
            )

        self.winner = True
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
