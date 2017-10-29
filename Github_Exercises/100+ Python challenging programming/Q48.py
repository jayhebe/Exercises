class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calc_area(self):
        return 3.14 * self.radius * self.radius
    
aCircle = Circle(2)
print(aCircle.calc_area())