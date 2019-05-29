from Rectangle import Rectangle
from Circle import Circle

if __name__ == '__main__':
    circle = Circle(int(input()))
    rectangle = Rectangle(int(input()),int(input()))
    circle.setColor(input())
    circle.setFilled(bool(input()))
    rectangle.setColor(input())
    rectangle.setFilled(bool(input()))
    print('Circle:')
    print('Radius is ',circle.getRadius())
    print('Diameter is ',circle.getDiameter())
    print('Area is ',circle.getArea())
    print('Perimeter is ',circle.getPerimeter())
    print(circle)

    print('Rectangle:')
    print('Width is ',rectangle.getWidth())
    print('Height is ',rectangle.getHeight())
    print('Area is ',rectangle.getArea())
    print('Perimeter is ',rectangle.getPerimeter())
    print(rectangle)
