class Course:
    def __init__(self, num: int, name:str, registered_students:int, max_students=50):
        self.num = num
        self.name = name
        self.registered_students = registered_students
        self.max_students = max_students

    def free_places(self):
        return self.max_students-self.registered_students

    def newly_registered_students(self, newly_registered_students:int):
        if newly_registered_students <= self.free_places:
            self.registered_students+=newly_registered_students
        else:
            self.registered_students=self.max_students

    def __str__(self):
        return f"Number of course: {self.num}, Name: {self.name}, Registered Students: {self.registered_students}"


num = int(input("Enter a number of course: "))
name = input("Enter a name of course: ")
registered_students = int(input("Enter a number of registered students: "))
max_students = int(input("Enter a number of max students: "))
my_course = Course(num, name, registered_students)
print(my_course)

