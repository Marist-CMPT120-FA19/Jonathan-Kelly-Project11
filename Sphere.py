#Jonathan Kelly, jonathan.kelly2@marist.edu
#creates a sphere object then calls methods inside the sphere class to return the surface area and volume

from math import *

class Sphere:

    def __init__(self, radius):
        self.radius= radius
        self.volume = ((4/3)*pi*(self.radius**3))
        self.surfaceArea = (4*pi*(self.radius**2))

    def Radius (self):
        return self.radius

    def Surfacearea(self):
        return self.surfaceArea

    def Volume(self):
        return self.volume
    
def main():
    
    radius= eval(input("What is the radius: "))
    s1= Sphere(radius)
    print("Volume is:", '%.2f'%s1.Volume())
    print("Surface Area is:", '%.2f'%s1.Surfacearea())
main()