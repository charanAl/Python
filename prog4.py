class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    def display_info(self):
        print(self.brand, self.color, self.year)

obj = Car('TATAnano','blue',2025)
obj1 = Car('BMW','black',2020)
obj3 = Car('Audi','white',2023)
obj.display_info()
obj1.display_info()
obj3.display_info()
# print(obj.brand)
# print(obj.color)