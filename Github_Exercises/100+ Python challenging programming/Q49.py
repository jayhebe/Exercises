class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calc_area(self):
        return self.length * self.width
    
rec = Rectangle(2.3, 8)
print(rec.calc_area())