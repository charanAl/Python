class Car:
    def __init__(self):
        self.brand = 'TaTa'
        self.color = 'Blue'
        self.year =  2026
        self.model = 'Nexon'
        self.price = 1500000
        self.milage = 20
        self.no_of_seats = 5
        self.no_of_doors = 4
        self.no_of_airbags = 6
        self.fuel_type = 'Petrol'
        self.transmission_type = 'Automatic'


    def travel(self):
            print("You can travel with this car")
        
    
obj1 = Car ()
print(obj1.brand)
print(obj1.color)
print(obj1.year)
print(obj1.milage)

obj1.travel()