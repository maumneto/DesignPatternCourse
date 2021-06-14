class GeometricFormat:
    def __init__(self, sideLength = 0, height = 0):
        self.sideLength = sideLength
        self.height = height
    
    def area_square(self):
        return sideLength * sideLength

    def perimeter_square(self):
        return sideLength * 4

    def area_triangle(self):
        area  = (sideLength * height)/2
        return area
    
    def draw_square(self):
        print("Drawing a Square!")

    def draw_triangle(self):
        print("Drawing a Triangle!")