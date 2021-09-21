import time


class TrafficLight:
    _color_ = ''

    def running(self):
        def timer(s):
            while s != 0:
                print(f'Осталось {s} секунд...')
                time.sleep(1)
                s -= 1

            return s

        self._color_ = 'Красный'
        print(f'{self._color_} цвет, ждите...')
        sec = 7
        timer(sec)
        self._color_ = 'Желтый'
        print(f'{self._color_} цвет, приготовтесь!')
        sec = 2
        timer(sec)
        self._color_ = 'Зеленый'
        print(f'{self._color_} цвет, вперед!!!')
        sec = 30
        timer(sec)


TrafficLight().running()
