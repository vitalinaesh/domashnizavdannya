class NS:
    def __init__(self, name: str, surname: str):
        if type(name) != str:
            raise TypeError('Name is not a string')
        if type(surname) != str:
            raise TypeError('Surname is not a string')
        self.name = name
        self.surname = surname

class Student:
    studentam = 0

    def __init__(self, name: str, surname: str, age: int, height: int = 160):
        if age <= 0:
            raise TypeError('Age must be greater than 0')
        self.height = height
        self.ns = NS(name, surname)
        self.age = age
        Student.studentam += 1

    def printst(self):
        print(f'Height: {self.height}')
        print(f'Name: {self.ns.name}')
        print(f'Surname: {self.ns.surname}')
        print(f'Age: {self.age}')

    def agebrth(self):
        self.age += 1
        print(f"Happy birthday to {self.ns.name}! Now you are {self.age} years old!")

try:
    frstudent = Student('Vitalina', 'Dunets', 0)
    frstudent.printst()
except Exception as error:
    print(f"Error: {error}")

print(f'Number of students: {Student.studentam}')