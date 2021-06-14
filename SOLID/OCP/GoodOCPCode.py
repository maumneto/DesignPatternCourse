class Vehicle:
    def __init__(self, value : float):
        self.value = value
    
    def getValue(self):
        return self.value

    def calculationPrice(self) -> float:
        printf('The price of generic vehicle is: %f' % getValue())
        return self.value


class Car(Vehicle):
    def __init__(self, value : float):
        super().__init__(value)

    def calculationPrice(self) -> float:
        return super().getValue() * 1.8


class Bike(Vehicle):
    def __init__(self, value : float):
        super().__init__(value)

    def calculationPrice(self) -> float:
        return super().getValue() * 1.4


if __name__ == '__main__':
    carro = Car(1000)
    print('Valor do Carro: %f' % carro.calculationPrice()) 
