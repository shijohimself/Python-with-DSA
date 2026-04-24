class Car:
    def set_info(self,color,type,mileage,seat_capacity):
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
    def set_audi_info(self,color,type,mileage,seat_capacity,electric,city):
        self.set_info(color,type,mileage,seat_capacity)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"This audi is {self.electric}")
        print(f"This audi is purchased in {self.city}")


c1 = Audi()
# c1.set_info("Black", "Diesel",22,2)
c1.set_audi_info("black","Diesel",12.4,7,"Manual","Bangalore")
c1.base_info()
c1.audi_info()
