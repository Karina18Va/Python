
from abc import ABCMeta, abstractmethod

import math

# abstract class
class Shape(metaclass=ABCMeta):
    def set_type(self, t):
        self.t = t

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):

        pass
    def intersect(self, obj):
        if obj.t == 'Rect' and self.t == 'Rect':
            print("intersect")
        elif   obj.t == 'circle' and self.t == 'Rect':
            pass


class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.t = 'circle'
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r**2

class Rectangle(Shape):
    def __init__(self, leftDownX, leftDownY, rightUpX, rightUpY):
        self.x1 = leftDownX
        self.y1 = leftDownY
        self.x2 = rightUpX
        self.y2 = rightUpY
        self.t = 'Rect'
    def perimeter(self):
        return 2*(self.x2 - self.x1) +2*(self.y2 - self.y1)
    def area(self):
        return (self.x2 - self.x1)*(self.y2 - self.y1)
if __name__ == '__main__':
    c = Circle(0,0,1)
    r = Rectangle(0,0,2,2)
    print("Circle area = {}".format(c.area(), c.perimeter()))
    print("Rectangle area = {}".format(r.area(), r.perimeter()))

    shapes = [c, r]
    for x in shapes:
        print("area = ", x.area())