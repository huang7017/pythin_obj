from GeometricObject import GeometricObject
class Rectangle(GeometricObject):
    def __init__(self,width = 1,height = 1,color = 'green',filled = True):
        super().__init__(color,filled)
        self.__height = height
        self.__width = width
    def setHeight(self,height):
        self.__height = height
    def setWidth(self,width):
        self.__width = width
    def getHeight(self):
        return self.__height
    def getWidth(self):
        return self.__width
    def getArea(self):
        return self.__height*self.__width
    def getPerimeter(self):
        return (self.__height+self.__width)*2
