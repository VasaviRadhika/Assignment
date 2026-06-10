import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        round(math.pi*self.radius**2)
    def perimeter(self):
        round(2*math.pi*self.radius)
a=Circle(10)
print(a.area())
print(a.perimeter())
