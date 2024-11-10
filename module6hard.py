# Наследование классов
import math
from gc import get_count, get_stats
from shutil import get_terminal_size


class Figure:
    def __init__(self, color, *data_list):
        self.__color = color
        self.__sides = []
        for j in range(1, len(data_list)):
            self.__sides.append(data_list[j])
        if len(self.__sides) != self.sides_count:
            self.__sides = []
            for side in range(self.sides_count):
                self.__sides.append(1)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if r < 0 or g < 0 or b < 0:
            return False
        elif r > 255 or g > 255 or b > 255:
            return False
        else:
            return True

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]

    def __is_valid_sides(self,*sides):
        condition = True
        for side in sides:
            if side < 0 or not isinstance(side,int) or len(sides) != self.__sides:
                condition = False
        return condition

    def get_sides(self):
        return self.__sides

    def  __len__(self):
        if self.sides_count == 1:
            p = self.__sides[0]
        elif self.sides_count == 3:
            p = self.__sides[0] + self.__sides[1] + self.__sides[2]
        elif self.sides_count == 12:
            p = self.__sides[0] * 12
        else:
            p = 0
        return  p

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(new_sides[i])


class Circle(Figure):
    def __init__(self, color, *data_list):
        self.sides_count = 1  # количество сторон
        super().__init__(color, *data_list)
        self.__radius = self.get_sides()[0] / 2 * math.pi

    def get_square(self):
        return self.__radius * self.__radius * math.pi


class Triangle(Figure):
    def __init__(self, color, *data_list):
        self.sides_count = 3
        super().__init__(color, *data_list)

    def get_square(self):
        return self.__sides[0] * self.__sides[1] / 2


class Cube(Figure):
    def __init__(self, color, *data_list):
        self.sides_count = 12
        super().__init__(color, *data_list)
        if len(self.get_sides()) == 1:
            for i in range(12):
                self.set_sides(data_list[1])

    def get_volume(self):
        return self.get_sides()[0] ** 3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # Пример
    c1 = Circle((200, 200, 100), 10, 15, 6) #, т.к.сторона у круга всего 1, то его стороны будут - [1]
    print(c1.get_sides())
    t1 = Triangle((200, 200, 100), 10, 6) # т.к.сторон у треугольника 3, то его стороны будут - [1, 1, 1]
    print(t1.get_sides())
    k1 = Cube((200, 200, 100), 9)# т.к.сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
    print(k1.get_sides())
    k2 = Cube((200, 200, 100), 9, 12)#т.к.сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
    print(k2.get_sides())