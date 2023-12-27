import math

# Using classes to make a room and conduct different mathematical operations.
# Math library.
# Constructor, static and class methods.
# Optional parameters.


class Room:

    # constructor method
    def __init__(self, width=1, length=1, height=1):
        self.width = width
        self.length = length
        self.height = height

    def calc_floor_area(self):
        return self.width * self.length

    def calc_floor_perimeter(self):
        return (self.width * 2) + (self.length * 2)

    def calc_volume(self):
        return self.width * self.height * self.length


roomOne = Room(2, 2)
print(roomOne.calc_floor_area())

roomTwo = Room(4, 6, 2)
print(roomOne.calc_floor_perimeter())
print(roomTwo.calc_floor_perimeter())

print(roomTwo.calc_volume())

# How classes can operate mathematical equations.
# Class and static methods.
# Mathematical equations.
# Math library.


class rightAngleTriangle:

    id = 0

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def hypot(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def calc_tri_area(self):
        return (self.x * self.y) / 2

    def calc_tri_perimeter(self):
        return self.x + self.y + self.hypot()

    @classmethod
    def get_id(cls):
        return cls.id

    @classmethod
    def display_attributes(cls, tris):
        print("ID \tHypot \tArea \tPerimeter")

        for i in range(len(tris)):
            triangle = tris[i]
            hypot = round(triangle.hypot())
            area = round(triangle.calc_tri_area())
            perimeter = round(triangle.calc_tri_perimeter())
            print(cls.id+(i+1), "\t\t", end="")
            print(hypot, "\t\t", end="")
            print(area, "\t\t", end="")
            print(perimeter, "\t\t", end="")
            print("\n")


triangleOne = rightAngleTriangle(4, 6)
triangleTwo = rightAngleTriangle(4)
triangleThree = rightAngleTriangle(9)
triangleFour = rightAngleTriangle(2, 15)

triangles = (triangleOne, triangleTwo, triangleThree, triangleFour)

demo = rightAngleTriangle()  # Creates a default object to show the method that displays the attributes of the triangle.

demo.display_attributes(triangles)


# How classes would come useful in extracting data from people

# Getter and Setter methods.
# Static methods.

class Employee:
    businessName = "Olivia's Company"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def get_gender(self):
        return self.gender

    def get_males(self):
        if self.gender == "M":
            return self.name
        else:
            return ""

    def get_females(self):
        if self.gender == "F":
            return self.name
        else:
            return ""

    @staticmethod
    def twenties(age):
        if 20 <= age < 30:
            return age
        else:
            return ""

    @staticmethod
    def display_employees(emp_list):

        print("Females \t\tMales \t\tTwenties")

        for j in range(len(emp_list)):
            emp = emp_list[j]
            print(emp.get_females(), "\t\t\t", end="")
            print(emp.get_males(), "\t\t\t", end="")
            print(emp.twenties(emp.get_age()), "\t\t\t", end="")
            print("\n")


empOne = Employee("Liv", 20, "F")
empTwo = Employee("Issy", 19, "F")
empThree = Employee("Josh", 17, "M")
empFour = Employee("Joanne", 52, "F")
empFive = Employee("Steve", 24, "M")
empSix = Employee("Brent", 27, "M")

emps = (empOne, empTwo, empThree, empFour, empFive, empSix)

empOne.display_employees(emps)

empOne.set_age(23)
empOne.display_employees(emps)
