from student import Student
students = list()
anton = Student("Anton", 10, 146, "C2015", "OOPPython", 12)
dima = Student("Dima", 15, 154, "C2015", "OOPPython", 11)
misha = Student("Misha", 12, 150, "C2015", "OOPPython", 10)
students.append(anton)
students.append(misha)
students.append(dima)
for student in students:
    print(student.__str__()) 