class Vehicle(object):
    def __init__(self, typeVehicle = None, value = 0):
        self.typeVehicle = typeVehicle
        self.value = value
    
    def getValue(self):
        return self.value

class Car(Vehicle):
    def __init__(self, typeInstance = None, value = 0):
        super(Car, self).__init__(typeInstance, value)

    def buyCar(self):
        print('buying a car...')

class Bike(Vehicle):
    def __init__(self, typeInstance = None, value = 0):
        super(Bike, self).__init__(typeInstance, value)

    def buyBike(self):
        print('buying a bike...')

class VehiclePrice:
    def calcVehiclePrice(self, Vehicle):
        if isinstance(Vehicle, Car):
            price = Vehicle.getValue() * 1.8
            print('buying a car! Price: %.2f' % price)
        elif isinstance(Vehicle, Bike):
            price = Vehicle.getValue() * 1.4
            print('buying a bike! Price %.2f' % price)
        else:
            print("There's no price calculation to %s" % type(Vehicle))

if __name__ == '__main__':
    car = Car('mercedez', 100000)
    price = VehiclePrice()
    price.calcVehiclePrice(car)

    bike = Bike('caloi', 1500)
    price = VehiclePrice()
    price.calcVehiclePrice(bike)

