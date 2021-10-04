from abc import ABC, abstractmethod


class WarehouseDesc:
    def __init__(self, number: int, length: int, width: int, height: int, address):
        self._number = number
        self._length = length
        self._width = width
        self._height = height
        self.address = address

    def __str__(self):
        return f'Склад №{self._number}, длинной:{self._length}, шириной:{self._width}, высотой:{self._height}, ' \
               f'рассположен по адресу:{self.address}.'


class OfficeEquipment(ABC):
    def __init__(self, name, number, weight, length, width, height):
        self.name = name
        self.number = number
        self._dimensions = {
            'Вес': weight,
            'Длинная': length,
            'Ширина': width,
            'Высота': height
        }

    def __str__(self):
        return f'Номер техники:{self.number}'

    @property
    def dimensions(self):
        return self._dimensions

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def features(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, number, weight, length, width, height, model, type_printing):
        super(Printer, self).__init__(name, number, weight, length, width, height)
        self.model = model
        self.type_printing = type_printing

    def get_name(self):
        return f'{self.name} {self.model}'

    def features(self):
        return f'Тип печати принтера: {self.type_printing}'


class Xerox(OfficeEquipment):
    def __init__(self, name, number, weight, length, width, height, model, type_color, supports):
        super().__init__(name, number, weight, length, width, height)
        self.model = model
        self.type_color = type_color
        self.supports = supports

    def get_name(self):
        return f'{self.name} {self.model}'

    def features(self):
        return f'Ксерокс поддерживает {self.type_color} печать, поддерживает {self.supports}'


class Scanner(OfficeEquipment):
    def __init__(self, name, number, weight, length, width, height, model, portable: bool, type_connection):
        super().__init__(name, number, weight, length, width, height)
        self.model = model
        self.portable = portable
        self.type_connection = type_connection

    def get_name(self):
        return f'{self.name} {self.model}'

    def features(self):
        return f'Портативность: {self.portable}, тип подключения: {self.type_connection}'


