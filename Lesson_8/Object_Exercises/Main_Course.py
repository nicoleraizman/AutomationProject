from Lesson_8.Object_Exercises import Course


num = int(input("Enter a number of course: "))
name = input("Enter a name of course: ")
registered_students = int(input("Enter a number of registered students: "))
new_registered_students = int(input("Enter a number of newly registered students: "))


my_course = Course(num, name, registered_students)
