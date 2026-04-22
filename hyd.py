students = ["charan", "cherry", "ram", "krishna"]

for i in range(len(students)):
    print(i+1,students[i])
# hyd = {student: "hyd" for student in students}
# hyd = [{"name": student, "house": "hyd"} for student in students]
# for student in students:
#     hyd.append({"name":student,"house":"hyd"})
# print(hyd)

# for student in sorted(hyd, key=lambda s: s["name"]):
#     print(student["name"])  