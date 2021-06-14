class Square:
    def __init__(self, sideLength = 0):
        self.sideLength = sideLength
    
    def area_square(self):
        return self.sideLength ** 2

    def perimeter_square(self):
        return self.sideLength * 4 

class Triangle:
    def __init__(self, base : float, height : float):
        self.base = base
        self.height = height
    
    def area_triangle(self):
        area = (self.base * self.height)/2
        return area

    def perimeter_square(self, hypotenuse = 0):
        perimeter = (self.base * 2) + hypotenuse
        return perimeter

if __name__ == '__main__':
    triangle = Triangle(10, 5.5)
    print('Triangle area: %f' % triangle.area_triangle())
    print('Triangle perimeter: %f' %triangle.perimeter_square(10))

    square = Square(10)
    print('Square area: %f' % square.area_square())
    print('Square perimeter: %f' % square.perimeter_square())
