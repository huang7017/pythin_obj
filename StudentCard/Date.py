class Date:
    def __init__(self,month,day,year):
        self.__month = month
        self.__day = day
        self.__year = year
    def setMonth(self,month):
        self.__month = month
    def getMonth(self):
        return self.__month
    def setDay(self,day):
        self.__day = day
    def getDay(self):
        return self.__day
    def setYear(self,year):
        self.__year = year
    def getYear(self):
        return self.__year
    def toString(self):
        return str(self.__month)+'\\'+str(self.__day)+'\\'+str(self.__year)
