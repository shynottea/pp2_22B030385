class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
        
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length**2
sh1 = Shape()
sq1 = Square(2)
print(sq1.area())
print(sh1.area())