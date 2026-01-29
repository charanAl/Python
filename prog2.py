class College:
    College_name = "Aurora's Technological Institutef"
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

s1 = College("Angle", 20, 85)
s2 = College('Aravind', 22, 90)
s3 = College('Charan', 20, 98)

print(s1.name)
print(s3.name)
print(s1.College_name)
print(s2.name)
print(s2.College_name)

        
