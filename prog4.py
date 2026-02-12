class Teacher:
    def __init__(self):
        self.name = 'Charan'
        self.__salary = 600000

    def get_salary(self):
        return self.__salary
a1 = Teacher()
print(a1.name)
print(a1.get_salary())