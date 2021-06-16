class DrawShape(object):
    def triangleDraw(self):
        raise NotImplementedError

    def squareDraw(self):
        raise NotImplementedError

    def circleDraw(self):
        raise NotImplementedError

class Triangle(DrawShape):
    def triangleDraw(self):
        print('Drawing a triangle...')

    def squareDraw(self):
        print('Drawing a square...')

    def circleDraw(self):
        print('Drawing a circle...')

class Square(DrawShape):
    def triangleDraw(self):
        print('Drawing a triangle...')

    def squareDraw(self):
        print('Drawing a square...')

    def circleDraw(self):
        print('Drawing a circle...')

class Circle(DrawShape):
    def triangleDraw(self):
        print('Drawing a triangle...')

    def squareDraw(self):
        print('Drawing a square...')

    def circleDraw(self):
        print('Drawing a circle...')


if __name__ == '__main__':
    triangle = Triangle()
    circle = Circle()
    square = Square()
    triangle.triangleDraw()
    circle.triangleDraw()
    square.triangleDraw()