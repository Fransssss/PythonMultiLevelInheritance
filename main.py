# author: Fransiskus Agapa

from school import School
from school import Teacher
from school import Student


def has_teacher(there_is_teacber):
    if there_is_teacber:
        print("The school has teacher")
    else:
        print("The school has no teacher")


def has_student(there_is_student):
    if there_is_student:
        print("The school has students")
    else:
        print("The school has students")


print("\n== School Database ==")
print("1. Print School")
print("2. Print Teacher")
print("3. Print Student")
choice = input("choice: ")

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n============")
        there_is_teacher = School.has_teacher
        there_is_student = School.has_student
        has_teacher(there_is_teacher)
        has_student(there_is_student)

    elif choice == '2':
        print("\n=============")
        teacher = Teacher()
        teacher.teach()

    elif choice == '3':
        print("\n=============")
        student = Student()
        student.teach()  # student's instance has access to teacher's
        student.study()

    else:
        print("\n[ Invalid choice ]")

    print("\n== School Database ==")
    print("1. Print School")
    print("2. Print Teacher")
    print("3. Print Student")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")
