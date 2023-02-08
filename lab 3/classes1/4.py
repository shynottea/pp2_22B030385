from math import *
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("x: ", self.x, "y: ", self.y)
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
    def dist(self, obj):
        return sqrt((self.x-obj.x)**2+(self.y-obj.y)**2)
p1 = Point(2, 4)
p2 = Point(-3, 1)
print(p1.dist(p2))