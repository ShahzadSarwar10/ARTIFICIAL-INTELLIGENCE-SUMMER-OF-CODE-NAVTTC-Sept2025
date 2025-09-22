#Polymorphism in + operator:
#We already know that the ‘+’ operator is frequently used in Python programs. However, it does not have a single application. When you wish to add two integers, concatenate two strings, or extend two lists, you use the same + sign. The + operator behaves differently depending on the type of object on which it is used.

a = 10
b = 20
print('Addition of 2 numbers:', a + b)

str1 = 'Hello '
str2 = 'Python'
print('Concatenation of 2 strings:', str1 + str2)

list1 = [1, 2, 3]
list2 = ['A', 'B']
print('Concatenation of 2 lists:', list1 + list2)

"""                    
Addition of 2 numbers: 30
Concatenation of 2 strings: Hello Python
Concatenation of 2 lists: [1, 2, 3, 'A', 'B']"""


#Polymorphism in * operator:
#The * operator is used to multiply 2 numbers if the data elements are numeric values. If one of the data types is a string, and the other is numeric, the string is printed that many times as that of the 2nd variable in the multiplication process.
a = 10
b = 5
print('Multiplication of 2 numbers:', a * b)

num = 3
mystr = 'Python'
print('Multiplication of string:', num * mystr)

"""Multiplication of 2 numbers: 50
Multiplication of string: PythonPythonPython"""



#Class Polymorphism in Python
#Because Python allows various classes to have methods with the same name, we can leverage the concept of polymorphism when constructing class methods. We may then generalize calling these methods by not caring about the object we’re working with. Then we can write a for loop that iterates through a tuple of items.
class Tiger():
    def nature(self):
        print('I am a Tiger and I am dangerous.')

    def color(self):
        print('Tigers are orange with black strips')

class Elephant():
    def nature(self):
        print('I am an Elephant and I am calm and harmless')

    def color(self):
        print('Elephants are grayish black')

obj1 = Tiger()
obj2 = Elephant()

for animal in (obj1, obj2): # creating a loop to iterate through the obj1 and obj2
    animal.nature()
    animal.color()

    """"I am a Tiger and I am dangerous.
Tigers are orange with black strips
I am an Elephant and I am calm and harmless
Elephants are grayish black"""



"""Polymorphism and Inheritance (Method Overriding)
Polymorphism is most commonly associated with inheritance. In Python, child classes, like other programming languages, inherit methods and attributes from the parent class. Method Overriding is the process of redefining certain methods and attributes to fit the child class. This is especially handy when the method inherited from the parent class does not exactly fit the child class. In such circumstances, the method is re-implemented in the child class. Method Overriding refers to the technique of re-implementing a method in a child class.
"""
class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show(self):
        print('Details:', self.brand, self.model, 'Price:', self.price)

    def max_speed(self):
        print('Vehicle max speed is 160')

    def gear_system(self):
        print('Vehicle has 6 shifter gearbox')

# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 260')

    def gear_system(self):
        print('Car has Automatic Transmission')

# Car Object
car = Car('Audi', 'R8', 9000000)
car.show()
# call methods from Car class
car.max_speed()
car.gear_system()

# Vehicle Object
vehicle = Vehicle('Nissan', 'Magnite', 550000)
vehicle.show()
# call method from a Vehicle class
vehicle.max_speed()
vehicle.gear_system()


""""Details: Audi R8 Price: 9000000
Car max speed is 260
Car has Automatic Transmission

Details: Nissan Magnite Price: 550000
Vehicle max speed is 160
Vehicle has 6 shifter gearbox"""

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
"""Circle
I am a two-dimensional shape.
Squares have each angle equal to 90 degrees.
153.93804002589985"""

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


"""Meow
I am a cat. My name is Kitty. I am 2.5 years old.
Meow
Bark
I am a dog. My name is Fluffy. I am 4 years old.
Bark"""