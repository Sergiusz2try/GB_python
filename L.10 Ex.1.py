class Matrix:
    def __init__(self, *args):
        self.value = list(args)

    def __str__(self):
        matrix = ''
        for el in self.value:
            matrix += f'{el} '
        return f'| {matrix}|'

    def __add__(self, other):
        sum_matrix = []
        for el_1, el_2 in zip(self.value, other.value):
            sum_matrix.append(el_1+el_2)
        return Matrix(*(el for el in sum_matrix))


mat1 = Matrix(1, 2, 4)
mat2 = Matrix(3, 6, 10)
print(mat1)
print(mat1 + mat2)
