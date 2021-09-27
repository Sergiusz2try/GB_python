from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    def consumption(self):
        return self._size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self._height = height

    @property
    def height(self):
        return self._height

    def consumption(self):
        return self._height*2 + 0.3


suit = Suit(190)
coat = Coat(52)
print(suit.height)
print(coat.size)
print(suit.consumption())
print(coat.consumption())
