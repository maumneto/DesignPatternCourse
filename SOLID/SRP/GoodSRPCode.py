class Square:
    def __init__(self, sideLength = 0):
        self.sideLength = sideLength
    
    def area_square(self):
        return sideLength ** 2

    def perimeter_square(self):
        return sideLength * 4 

class Triangle:
    def __init__(self, base = 0, height = 0):
        self.base = base
        self.height = height
    
    def area_triangle(self):
        area = (base * height)/2
        return area

    def perimeter_square(self, hypotenuse):
        perimeter = (sideLength * 2) + hypotenuse
        return perimeter