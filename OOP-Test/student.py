class Student:

    first_name = ''
    last_name = ''
    grade = 0

    def __int__(self):
        self.first_name = "John"
        self.last_name = "doe"
        self.grade = 0

    def new_student(self, firstname, lastname, grade):
        self.first_name = firstname
        self.last_name = lastname
        self.grade = int(grade)

    def get_student(self):
        return self
