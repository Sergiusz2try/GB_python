class Cell:
    def __init__(self, amount: int):
        self._amount = amount

    def __str__(self):
        return f'Количество ячеек в клетке:{self._amount}'

    def __add__(self, other):
        return self._amount + other._amount

    def __sub__(self, other):
        if self._amount - other._amount >= 0:
            return self._amount - other._amount
        else:
            print('Только если разность количества ячеек двух клеток больше нуля.')

    def __mul__(self, other):
        return Cell(self._amount * other._amount)

    def __truediv__(self, other):
        return Cell(self._amount / other._amount)

    @property
    def amount(self):
        return self._amount

    def make_order(self, value_in_place):
        i = self._amount // value_in_place
        result = ('*' * value_in_place + '\n') * i
        b = self._amount - i * value_in_place
        result += '*' * b
        return result


cell_1 = Cell(16)
cell_2 = Cell(23)
print(cell_2 + cell_1)
print(cell_2 - cell_1)
print(cell_2 * cell_1)
print(cell_2 / cell_1)
print(cell_2.make_order(6))
