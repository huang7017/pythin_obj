import math
from GeometricObject import GeometricObject
class Circle(GeometricObject):
    def __init__(self,radius = 1,color = 'Green',filled = True):
        super().__init__(color,filled)
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def setRadius(self,radius):
        self.__radius = radius
    def getArea(self):
        return self.__radius*self.__radius*math.pi
    def getDiameter(self):
        return int(self.__radius)*2
    def getPerimeter(self):
        return self.__radius*2*math.pi
