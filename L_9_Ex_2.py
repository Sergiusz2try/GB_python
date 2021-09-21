class Road:

    def __init__(self, length, width):
        self.__length__ = length
        self.__width__ = width

    def weight_road(self):
        weight = f'{self.__length__ * self.__width__ * 25 * 5 / 1000} т'

        return weight


road_1 = Road(20, 5000)
road_2 = Road(10, 100)
print(road_1.weight_road())
print(road_2.weight_road())
