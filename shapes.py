import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area (self):
        A = math.pi * self.radius**2
        return A
    def circumference (self):
        C = 2 * math.pi * self.radius
        return C


class Square:
    def __init__(self,side):
        self.side = side
    def area (self):
        A = self.side ** 2
        return A
    def perimeter (self):
        P = 4 * self.side
        print(P)


class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area (self):
        A = self.width * self.length
        print(A)
    def perimeter (self):
        P = 2 * (self.length + self.width)
        print(P)
    
    
class Sphere:
    def __init__(self,raduis):
        self.radius = raduis
    def area (self):
        A = 4 * math.pi * self.radius**2
        print(A)
    def volume (self):
        V = 4/3 * (math.pi * self.radius**3)
        print(V)



