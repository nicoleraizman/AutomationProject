from Lesson_11.Student import Student

class Course:
    def __init__(self, num_of_course, name_of_course, max_students):
        self.num_of_course = num_of_course
        self.name_of_course = name_of_course
        self.max_students = max_students
        self.list_of_students = []
        self.list_of_subjects_and_teachers = {}

    def __str__(self):
        return f"Number of course: {self.num_of_course}, Name of course: {self.name_of_course}, Maximal number of students: {self.max_students}"

    def __repr__(self):
        return f"Subjects and teachers: {self.list_of_subjects_and_teachers}, Name of a student: {self.name_of_student}, Subjects and grades: {self.subjects_and_grades}"

    def add_student(self, student):
        for student in self.list_of_students:
            if len(self.list_of_students) <= self.max_students:
                self.list_of_students.append(student)
                return True
            else:
                return False

    def add_factor(self, subject, factor):
        for student in self.list_of_students:
            student.calc_factor(subject, factor)

    def del_student(self, Student):
        del Course["Student"]

    def averages(self):
        return [average for i in range(list_of_averages)]

    def weak_students(self):
        return min(self.list_of_students.index())

