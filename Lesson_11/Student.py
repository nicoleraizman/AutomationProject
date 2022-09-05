class Student:
    def __init__(self, id1:int, name:str, age:int, subject_and_grade:dict):
        self.id = id1
        self.name_of_student = name
        self.age_of_student = age
        self.subjects_and_grades = {}

    def add_grade(self, subject, grade):
        self.subjects_and_grades[subject] = grade

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name_of_student}, Age: {self.age_of_student}, Subject and grade: {self.subjects_and_grades}"

    def calc_factor(self, subject, factor):
        grade_with_factor =  (self.subjects_and_grades[subject]*factor/100) + self.subjects_and_grades[subject]
        if grade_with_factor >= 100:
            grade_with_factor == 100

    def average(self, grades):
        avg = sum(self.subjects_and_grades.values())/len(self.subjects_and_grades.values())
        return avg

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

st1=Student(id1, name, age, subject_and_grade)