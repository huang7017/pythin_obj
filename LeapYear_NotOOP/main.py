def isLeapYear(newYear):
        if ((newYear%4 == 0) & (newYear%100 != 0) | (newYear%400 == 0)):
            return True
        else:
            return False
if __name__ == '__main__':
    for i in range(3):
        y = int(input())
        if (isLeapYear(y)):
            print('The ',y, ' is leap year.')
        else:
            print('The ',y,' isn\'t  leap year.')
