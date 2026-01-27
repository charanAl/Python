class Student:
    def __init__(self, name, age,marks=100):
        self.name = name
        self.age = age
        self.marks = marks

    def attend_class(self):
            print("Thanks for attending the session")
    def show_grade(self):
            return " you have Good Grades A!"
        
obj = Student("Charan", 21, 96)
print(obj.name)
print(obj.marks)
print(obj.age)
print(obj.show_grade())