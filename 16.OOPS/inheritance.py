class Car:
    def __init__(self,color, type,mileage,seat_capacity):
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity
    
    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"seat capacity = {self.seat_capacity}")
        
class Audi(Car):
    def __init__(self):
        print("Audi init")

c1 = Car("Black","Petrol",22.5,7)
c1.base_info()

audi_car = Audi()
audi_car.color = "black"
audi_car.type = "diesel"
audi_car.mileage = 30
audi_car.seat_capacity = 2
audi_car.base_info()
