class student:

    def __init__(self, name, grade):
        self.student_name = name
        self.student_grade = grade

    def setgrade(self, grade):
        self.student_grade = grade

    def getgrade(self):
        return self.student_grade

    def print_student_info(self):
        print("the students name is %s" % self.student_name)
        print("the students grade is %s" % self.student_grade)
