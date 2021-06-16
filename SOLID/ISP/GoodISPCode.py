class DrawShape(object):
    def draw(self):
        raise NotImplementedError

class Circle(DrawShape):
    def draw(self):
        print('Drawing a circle...')

class Square(DrawShape):
    def draw(self):
        print('Drawing a square...')

class Triangle(DrawShape):
    def draw(self):
        print('Drawing a triangle...')

if __name__ == '__main__':
    circle = Circle()
    triangle = Triangle()
    square = Square()
    circle.draw()
    square.draw()
    triangle.draw()