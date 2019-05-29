from Student import Student
from Date import Date

if __name__ == '__main__':
    s1 = Student('Johin',Date(6,1,1999),90)
    s2 = Student('Marry',Date(10,8,1997),80)
    s1.setName(input())
    set = Date(input(),input(),input())
    s2.setDate(set)
    print(s1.toString())
    print(s2.toString())
