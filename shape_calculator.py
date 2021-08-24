import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        counter = self.height
        shape = "*"
        lines = ""

        if (self.height > 50 or self.width > 50):
            return "Too big for picture."

        while (counter > 0):
            lines += (shape * self.width) + "\n"
            counter -= 1

        return lines

    def get_amount_inside(self, shape):
        return math.floor(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side

    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_height(self, height):
        self.height = height
        self.width = height
        self.side = height

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width
