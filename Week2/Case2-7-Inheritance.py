#Create a Parent Class
#Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

#Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

    #Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Next  run
print (" Next  run")


#Python Inheritance
#Being an object-oriented language, Python supports class inheritance. It allows us to create a new class from an existing one.
#The newly created class is known as the subclass (child or derived class).
#The existing class from which the child class inherits is known as the superclass (parent or base class).

class Animal:

    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):
    
    # override eat() method
    def eat(self):
        
        # call the eat() method of the superclass using super()
        super().eat()
        
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

labrador.eat()

print(Dog.mro())

# Next  run
print (" Next  run")

class Bird:
    def fly(self):
        print("The bird is flying...")

class Mammal:
    def run(self):
        print("The mammal is running...")

class Bat(Bird, Mammal):
    pass

b = Bat()
b.fly()         # Output: The bird is flying...
b.run()         # Output: The mammal is running…


# Next  run
print (" Next  run")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("The animal is eating...")

class Dog(Animal):
    def bark(self):
        print("Woof woof!")

d = Dog("Rover", 3)
print(d.name)   # Output: Rover
d.eat()         # Output: The animal is eating...
d.bark()        # Output: Woof woof!