from math import pi
class Shape:
    def __init__(self,name) -> None:
        self.name = name

class Rectangular(Shape):
    def __init__(self, name,length,width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name,radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius
    

rantangular_area = Rectangular('Rectangular Area',7,5)
rectangular_result = rantangular_area.area()
print(rectangular_result)
circle_area = Circle('Circle Area', 5)
circle_result = circle_area.area()
print(circle_result)