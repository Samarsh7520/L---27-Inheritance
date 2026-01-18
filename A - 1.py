class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name 
        self.max_speed = max_speed 
        self.mileage = mileage 

class BMW(Vehicle):
    pass 

car1 = BMW("BMW",200,100)
print("Car Name: ",car1.name)
print("Car Max Speed: ",car1.max_speed)
print("Car Mileage: ",car1.mileage)