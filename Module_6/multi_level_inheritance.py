# multi level inheritance class
class Vehicle:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUpTrack(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat,temparature) -> None:
        self.temparature = temparature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        return f'Bus Name: {self.name}. Bus Price: {self.price}. Bus Seat: {self.seat}. Temparature: {self.temparature}.'
        return super().__repr__()
    

emad = AcBus('Emad Paribahan', 5000000, 25, '16 Degree')
print(emad)