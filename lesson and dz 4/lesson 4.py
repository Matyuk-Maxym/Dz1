import math


class Shape:
    width = 0
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    # def __init__(self, width, height):
    #     self.width = width
    #     self.height = height

    degree = 0

    def __init__(self, width, height):
        super().__init__(width, height)
        self.degree = 90

    def draw(self):
        print("Drawing" + str(self.width) + "x" + str(self.height))


    def area(self):
        print(self.width * self.height)


class ColorRectangle(Rectangle):
    color = ""
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color

    def draw(self):
        super().draw()
        print(self.color)


class Parallelogram(Rectangle):
    def __init__(self, width, height,degree):
        super().__init__(width, height)
        super().degree =  degree



class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

    def draw(self):
        print("Drawing")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Drawing")
        print(self.radius)

    def area(self):
        print(math.pi * math.pow(self.radius, 2))


rectangle = Rectangle(5, 5)
circle = Circle(5)

rectangle.area()
circle.area()


colorRectangle = ColorRectangle(5, 5, "red")
colorRectangle.draw()


