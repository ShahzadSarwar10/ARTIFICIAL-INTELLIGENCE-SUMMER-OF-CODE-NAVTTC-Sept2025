class Person:
    isRegisteredInLabDB=None
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

# create object of a class
jessa = Person('Jessa', 'Female', 'Software Engineer')
# create object of a class
richard = Person('Richard', 'Male', 'Project Manager')

print(Person.isRegisteredInLabDB)
print(jessa.name)
print(jessa.profession)

#print(Person.profession)

# call methods
jessa.show()
jessa.work()

#Set Class variable
Person.isRegisteredInLabDB="TrueYesRegisteredPerson"
print(Person.isRegisteredInLabDB)

# call methods
richard.show()
richard.work()

print(Person.isRegisteredInLabDB)

#build-in Method   __str__
StringVar="This is test case"
intVar = 344
print(StringVar.__str__())
print(richard.__str__())
print(richard)


# Next  run
print (" Next  run")
# a simple exmaple of class
# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the properties 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()

"""In the above example, we have created a class named Room with:
Attributes: length and breadth
Method: calculate_area()"""


# Next  run
print (" Next  run")

#All classes have a function called __init__(), which is always executed when the class is being initiated.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# Next  run
print (" Next  run")

#All classes have a function called __init__(), which is always executed when the class is being initiated.
#The __str__() Function - The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Next  run
print (" Next  run")
#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
   
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Next  run
print (" Next  run")

#Muliptle constructor - in Python - doesn't exist
#Workaround - The easiest way is through keyword arguments:
class City():
  def __init__(self, city=None, Long = None, lat =None):
    pass

someCity = City(city="Berlin")


# Next  run
print (" Next  run")
#Accessing properties and assigning values
#   An instance attribute can be accessed or modified by using the dot notation: instance_name.attribute_name.
#   A class variable is accessed or modified using the class name
class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)



"""Garbage Collection(Destroying Objects) in Python
Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space. The process by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes."""

#Example
#The __del__() destructor prints the class name of an instance that is about to be destroyed as shown in the below code block −
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

"""Data Hiding in Python
An object's attributes may or may not be visible outside the class definition. You need to name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders."""

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)


# Next  run
print (" Next  run")
#three method types differ from one another, then consider the following overview that compares them:
# Instance methods use a self parameter pointing to an instance of the class. They can access and modify instance state through self and class state through self.__class__. These are the most common methods in Python classes.
# Class methods use a cls parameter pointing to the class itself. They can modify class-level state through cls, but they can’t modify individual instance state.
# Static methods don’t take self or cls parameters. They can’t modify instance or class state directly, and you’ll mainly use them for organizational purposes and namespacing.
class DemoClass:
    def instance_method(self):
        return ("instance method called", self)

    @classmethod
    def class_method(cls):
        return ("class method called", cls)

    @staticmethod
    def static_method():
        return ("static method called",)
    

# Next  run
print (" Next  run")
class Student:
    def __init__(self, roll_no): self.roll_no = roll_no

    # instance method
    def show(self):
        print('In Instance method')

    @classmethod
    def change_school(cls, name):
        print('In class method')

    @staticmethod
    def find_notes(subject_name):
        print('In Static method')

# create two objects
jessa = Student(12)

# instance method bound to object
print(jessa.show)

# class method bound to class
print(jessa.change_school)

# static method bound to class
print(jessa.find_notes)



# Next  run
print (" Next  run")
#Static Method
#Static methods are ideal for utility functions that don't depend on the instance or class state. They are defined using the @staticmethod decorator and are not bound to the instance or class. Let's consider a real-world example where a static method is beneficial.
#Example: Date Manipulation
from datetime import date

class DateUtils:
   
    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year."""
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False

# Usage
year = 2024
if DateUtils.is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 


# Next  run
print (" Next  run")
#Instance Method
#Instance methods operate on an instance of the class and have access to instance-specific data. They are the default type of methods in Python. Let's explore a scenario where instance methods are the most appropriate choice.
#Example: Bank Account
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

# Usage
account = BankAccount(account_holder="Alice", balance=1000)
account.deposit(500)
account.withdraw(200) 


#Example of Different Method Types
class MethodTypes:

    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)
            
    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)
       # print(cls.lastname)
        print()
    @staticmethod
    def staticMethod():
        print("This is a static method")
       # print(name)

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()