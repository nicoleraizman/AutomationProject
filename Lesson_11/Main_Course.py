from Lesson_11.Course import Course
from Lesson_11.Student import Student

num_of_course = int(input("Enter number of a Course: "))
name_of_course = input("Enter name of a Course: ")
max_students = int(input("Enter max of the students: "))
c1 = Course(num_of_course, name_of_course, max_students)

print(c1)


for subject in range(5):
    subject = input("Enter name of a subject: ")
    teacher = input("Enter name of a teacher: ")
    c1.list_of_subjects_and_teachers[subject] = teacher
print(c1.list_of_subjects_and_teachers)


id1 = int(input("Enter student's ID: "))
while id1 != 0 and c1.add_student != False:
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    st1 = Student(id1,name,age)
    for subject in st1.subjects_and_grades:
        grade = int(input("Enter a grade: "))
        st1.subjects_and_grades[subject] = grade

    st1.id = int(input("Enter student's ID: "))





