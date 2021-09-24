class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print('Релевантность — это обозначение субъективной степени соответствия чего-либо в моменте времени.')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print('Синий кит – самое крупное животное из отряда китообразные, а также самое больший живой организм из '
              'ныне обитающих на Земле.')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print('Типология мышления — встречающаяся в психологической науке классификация видов и типов мышления. В '
              'различных концепциях и отраслях психологии встречаются различные классификации и типологии мышления.')


draw_1 = Stationery('Тест №1')
draw_1.draw()
pen = Pen('Тест №2')
pen.draw()
pencil = Pencil('Тест №3')
pencil.draw()
handle = Handle('Тест №4')
handle.draw()