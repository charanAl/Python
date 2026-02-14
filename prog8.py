class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.model = 'Nexon'
        self.price = 1500000

    def travel(self):
        print('You can travel with This Car!')

    def printAll(self):
        print(self.brand,self.color,self.year,self.model,self.price)

car1 = Car('Tata', 'Blue',2024)
car1.printAll()