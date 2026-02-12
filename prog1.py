#Bunding the data & method into one class =ENCAPSULATION
class Student:
    def __init__(self):
        self.name = 'charan'
        self._age = 22
        self.__grade= 'A'

s1 =Student()
print(s1.name) 
print(s1._age ) 
print(s1.__grade)    
