# Module 8
#   Programming Assignment 11
#     Prob-2.py

# Your code below


class Student:
    def __init__(self, name, id_num, major, gpa):
        self._name = name
        self._id = id_num
        self._major = major
        self._gpa = gpa

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_major(self):
        return self._major

    def get_gpa(self):
        return self._gpa

    def set_name(self, name):
        self._name = name

    def set_id(self, id):
        self._id = id

    def set_major(self, major):
        self._major = major

    def set_gpa(self, gpa):
        self._gpa = gpa


def testStudent(students):

    for student in students:
        print(student.get_id(), student.get_gpa(),
              student.get_name(), student.get_major())

    for i in range(0, len(students)):
        students[i].set_name(students[i].get_name() + "_" + str(i))
        students[i].set_id(students[i].get_id() + i)
        students[i].set_major(students[i].get_major() + "_" + str(i))
        students[i].set_gpa(students[i].get_gpa() + i)

    for student in students:
        print(student.get_id(), student.get_gpa(),
              student.get_name(), student.get_major())


if __name__ == "__main__":
    students = []
    student0 = Student("Joe Bella", 9933, "Web Development", 3.8)
    student1 = Student("Tucker Blank", 3399, "Nursing", 3.0)
    student2 = Student("Gayle Ujifusa", 1011, "Baking", 2.8)
    student3 = Student("Edna Anker", 9875, "Medical Office", 3.0)
    students.append(student0)
    students.append(student1)
    students.append(student2)
    students.append(student3)

    testStudent(students)
