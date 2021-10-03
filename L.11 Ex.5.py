from abc import ABC, abstractmethod


class WarehouseDesc:
    def __init__(self, number: int, length: int, width: int, height: int, address):
        self._number = number
        self._length = length
        self._width = width
        self._height = height
        self.address = address
        self.equipment = {}

    def __str__(self):
        return f'Склад №{self._number}, длинной:{self._length}, шириной:{self._width}, высотой:{self._height}, ' \
               f'рассположен по адресу:{self.address}.'

    def add_equipment(self, equipment):
        if not equipment.name_class() in self.equipment:
            self.equipment[equipment.name_class()] = 1
        else:
            new_value = self.equipment.get(equipment.name_class()) + 1
            self.equipment[equipment.name_class()] = new_value


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

    @staticmethod
    def name_class():
        return 'Printer'

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

    @staticmethod
    def name_class():
        return 'Xerox'

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

    @staticmethod
    def name_class():
        return 'Scanner'

    def get_name(self):
        return f'{self.name} {self.model}'

    def features(self):
        return f'Портативность: {self.portable}, тип подключения: {self.type_connection}'


warehouse1 = WarehouseDesc(666, 2000, 1000, 200, 'Orzeshko 1b')
xerox1 = Xerox('Canon', 123, 5.6, 115, 45, 56, 'Tx-3000', 'Black-white', 'Wi-Fi')
xerox2 = Xerox('HP', 124, 5.6, 115, 45, 56, 'XR-150', 'Black-white', 'Wi-Fi')
warehouse1.add_equipment(xerox1)
print(warehouse1.equipment)
warehouse1.add_equipment(xerox2)
print(warehouse1.equipment)
printer1 = Printer('Hp', 120, 5, 100, 30, 45, 'IQ-max', 'Laser')
printer2 = Printer('Hp', 111, 5, 80, 20, 35, 'IQ-mini', 'Laser')
scanner1 = Scanner('Toshiba', 101, 3, 76, 40, 30, 'Hyper-Tank', True, 'USB')
warehouse1.add_equipment(printer1)
warehouse1.add_equipment(printer2)
warehouse1.add_equipment(scanner1)
print(warehouse1.equipment)
