#Abstract Class
#In Python, an abstract class is a class that cannot be instantiated on its own and is meant to be subclassed by other classes. Abstract classes are created using the abc (Abstract Base Classes) module. Abstract classes may contain abstract methods, which are methods that are declared in the abstract class but don't have an implementation. Subclasses of the abstract class are required to provide implementations for these abstract methods.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Example usage:
circle = Circle(radius=5)
square = Square(side_length=4)

print("Circle Area:", circle.area())          # Output: 78.5
print("Square Area:", square.area())            # Output: 16





#Create an empty class and set attributes for different objects

class Amit:
   pass

# Creating objects
ob1 = Amit()
ob2 = Amit()

# Displaying
print(ob1)
print(ob2)


class Student:
   pass
# Creating objects
st1 = Student()
st1.name = 'Henry'
st1.age = 17
st1.marks = 90

st2 = Student()
st2.name = 'Clark'
st2.age = 16
st2.marks = 77
st2.phone = '120-6756-79'

print('Student 1 = ', st1.name, st1.age, st1.marks)
print('Student 2 = ', st2.name, st2.age, st2.marks, st2.phone)


#What is a Data Class in Python 
#In Python, a data class is a class that is primarily used to store data, and it is designed to be simple and straightforward. Data classes are introduced in Python 3.7 and later versions through the data class decorator in the data classes module.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: str
    major: str
    year: str
    gpa: float

julia = Student('Julia',0.5,'Statistics','sophomore','who cares!')

print(julia)
print(julia.name)
print(julia.year)