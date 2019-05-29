class GeometricObject:
    def __init__(self,color,filled):
        self.__color  = color
        self.__filled = filled
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setFilled(self,filled):
        self.__filled = filled
    def isFilled(self):
        return self.__filled
    def __str__(self):
        return 'color: '+str(self.__color)+' and filled: '+str(self.__filled)
