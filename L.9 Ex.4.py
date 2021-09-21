import random


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.real_speed = 0

    def go(self):
        print(f'{self.name} поехал и постепенно набирает скорость...')
        self.real_speed = random.randint(20, self.speed)

    def stop(self):
        print(f'{self.name} остановился.')
        self.real_speed = 0

    def turn(self, direction):
        if direction == 'Right':
            print(f'{self.name} остановилась и повернула направо!')
            self.go()
        elif direction == 'Left':
            print(f'{self.name} остановилась и повернула налево!')
            self.go()
        else:
            print(f'{self.name} продолжает движение прямо!')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.real_speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name)

    def show_speed(self):
        if self.real_speed > 60:
            print(f'{self.name} превысил допустимую скорость 60 км/ч и движется со скоростью {self.real_speed} км/ч')
        else:
            print(f'{self.name} движется со скоростью {self.real_speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name)

    def show_speed(self):
        if self.real_speed > 40:
            print(f'{self.name} превысил допустимую скорость 40 км/ч и движется со скоростью {self.real_speed} км/ч')
        else:
            print(f'{self.name} движется со скоростью {self.real_speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super(PoliceCar, self).__init__(speed, color, name, is_police)


car_1 = Car(1200, 'Black', 'Mustang')
car_1.go()
car_1.show_speed()
car_1.turn('Right')
car_1.show_speed()
car_1.stop()

car_2 = TownCar(120, 'Blue', 'Carola')
car_2.go()
car_2.turn('Left')
car_2.show_speed()
car_2.go()
car_2.show_speed()
car_2.stop()