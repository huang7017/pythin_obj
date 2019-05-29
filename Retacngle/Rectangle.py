class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def setLength(self,length):
        self.__length = length
    def setWidth(self,width):
        self.__width = width
    def getLength(self):
        return self.__length
    def getWidth(self):
        return self.__width
    def getArea(self):
        return self.__length*self.__width
    def getPerimeter(self):
        return (self.__length+self.__width)*2
