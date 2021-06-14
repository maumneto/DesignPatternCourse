class GeometricFormat(object):
    def __init__(self, sideLength = 0, height = 0):
        self.sideLength = sideLength
        self.height = height
    
    def area_square(self):
        return self.sideLength ** 2

    def perimeter_square(self):
        return self.sideLength * 4

    def area_triangle(self):
        area  = (self.sideLength * self.height)/2
        return area
    
    def draw_square(self):
        print("Drawing a Square!")

    def draw_triangle(self):
        print("Drawing a Triangle!")


if __name__ == '__main__':
    square = GeometricFormat(10, 3)
    print('Square area: %f' % square.area_square())