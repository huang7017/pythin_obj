from Student import Student
from Date import Date

if __name__ == '__main__':
    s1 = Student('Johin',Date(6,1,1999),90)
    s2 = Student('Marry',Date(10,8,1997),80)
    name = input()
    month = input()
    day = input()
    year = input()
    s1.setName(name)
    set = Date(month,day,year)
    s2.setDate(set)
    print(s1.toString())
    print(s2.toString())
