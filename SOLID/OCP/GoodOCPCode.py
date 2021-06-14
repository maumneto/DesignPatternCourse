class Vehicle(object):
    def __init__(self, value = 0):
        self.value = value
    
    def getValue(self):
        return self.value

    def calculationPrice(self):
        print('The price of generic vehicle is: %f' % getValue())
        return self.value


class Car(Vehicle):
    def __init__(self, value = 0):
        super(Car, self).__init__(value)

    def calculationPrice(self):
        return super().getValue() * 1.8


class Bike(Vehicle):
    def __init__(self, value):
        super(Bike, self).__init__(value)

    def calculationPrice(self):
        return super().getValue() * 1.4


if __name__ == '__main__':
    car = Car(100000)
    print('Value of the car: %f' % car.calculationPrice()) 

    bike = Bike(1000)
    print('Value of the car: %f' % bike.calculationPrice()) 
