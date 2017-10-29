class Shape():
    def calc_area(self):
        return 0
        
class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def calc_area(self):
        return self.length ** 2
    
s = Shape()
print(s.calc_area())
ss = Square(6)
print(ss.calc_area())