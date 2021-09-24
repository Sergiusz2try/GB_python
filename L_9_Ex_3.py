class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income__ = {
                            'wage': income,
                            'bonus': income * 0.2
                          }


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}')

    def get_full_income(self):
        wage = self.__income__.get('wage')
        bonus = self.__income__.get('bonus')
        print(f'Зарплата с учетом бонуса в 20%: {int(wage+bonus)}$')


worker_1 = Position('David', 'Abramov', 'Driver', 1200)
worker_1.get_full_name()
worker_1.get_full_income()
