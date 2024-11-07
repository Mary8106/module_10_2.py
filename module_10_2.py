from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.kname}, на нас напали!')
        enemy = 100
        day = 0
        while enemy > 0:
            sleep(1)
            day += 1
            enemy -= self.power
            if enemy < 0:
                enemy = 0
            print(f'{self.kname} сражается {day}, осталось {enemy} воинов')
        print(f'{self.kname} одержал победу спустя {day} дней(дня)!')


def main():
    knight1 = Knight('Sir Lancelot', 10)
    knight2 = Knight('Sir Galahad', 20)

    knight1.start()
    knight2.start()
    knight1.join()
    knight2.join()

    print('Все битвы закончены!')

if __name__ == '__main__':
    main()

