from Rectangle import Rectangle


if __name__ == '__main__':
    l1 = int(input())
    l2 = int(input())
    w1 = int(input())
    w2 = int(input())
    r1 = Rectangle(l1,w1)
    r2 = Rectangle(l2,w2)

    print(r1.getArea(),' ',r1.getPerimeter())
    print(r2.getArea(),' ',r2.getPerimeter())
    r2.setLength(50)
    r2.setWidth(25)
    print(r2.getArea(),' ',r2.getPerimeter())
