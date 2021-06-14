class Vehicle:
    def __init__(self, typeVehicle : str, value : float):
        self.typeVehicle = typeVehicle
        self.value = value
    
    def getValue(self) -> float:
        return value
    
class VehiclePrice:
    def calcVehiclePrice(self, Vehicle vehicle) -> float:
        if (type(vehicle) == Car):
            return vehicle.getValue() * 0.8
        elif (type(vehicle) == Bike):
            return vehicle.getValue() * 0.4
        else:
            print("There's no price calculation to %s" % type(vehicle))
