
class School:

    has_teacher = True
    has_student = True


class Teacher(School):

    def teach(self):
        print("Teacher is teaching")


class Student(Teacher):

    def study(self):
        print("Students are studying")

