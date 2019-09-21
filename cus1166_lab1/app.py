from mymodules.models import Student
from mymodules.math_utils import average_grade
roster = []

roster.append(Student("Tim", 88))
roster.append(Student("Jam", 74))
roster.append(Student("Steve", 100))
roster.append(Student("Ray", 85))
roster.append(Student("Charlie", 86))
roster.append(Student("Angela", 70))
roster.append(Student("Lidia", 60))
roster.append(Student("Rose", 90))
roster.append(Student("Navi", 78))
roster.append(Student("Larry", 0))

for student in roster:
    student.print_student_info()

print("The average grade is " + str(average_grade(roster)))