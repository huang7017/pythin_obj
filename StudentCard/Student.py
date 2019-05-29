from Date import Date

class Student:
    def __init__(self,name,date,score):
        self.__name = name
        self.__date = date
        self.__score = score
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.name
    def setDate(self,date):
        self.__date = date
    def getDate(self):
        return self.__Date
    def setScore(self,score):
        self.__score = score
    def getScore(self):
        return self.__score
    def toString(self):
        return str(self.__name)+ ' '+str(self.__date.toString())+ ' ' + str(self.__score)
