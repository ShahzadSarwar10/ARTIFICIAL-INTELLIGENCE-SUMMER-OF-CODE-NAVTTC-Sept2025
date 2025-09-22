# Next  run
print (" Next  run")

# Reference: https://blog.ravikiran.me/2023/09/inheritance-explained-python/
#Simple inheritance, also known as single inheritance, is the most basic form of inheritance. In simple inheritance, a class inherits properties and behaviors (attributes and methods) from a single parent class. This type of inheritance is used to create a new class that is a specialized version of the parent class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

#Multiple Inheritance
#Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes. This means that a class can have more than one parent class. Python supports multiple inheritance, but it should be used with caution to avoid potential conflicts and ambiguity.

class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

#Multi-level Inheritance
#Multi-level inheritance involves creating a chain of classes where each class inherits from the one above it. This forms a hierarchy of classes, and each subclass inherits the properties and behaviors of its parent class.

class Grandparent:
    def method_grandparent(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def method_parent(self):
        print("Method from Parent")

class Child(Parent):
    def method_child(self):
        print("Method from Child")


#Hierarchical Inheritance
#Hierarchical inheritance occurs when multiple classes inherit from a single parent class. In this scenario, several child classes share a common base class, allowing code reuse and specialization.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

#Hybrid Inheritance
#Hybrid inheritance is a combination of two or more types of inheritance. It can involve any combination of simple, multiple, multi-level, and hierarchical inheritance. While Python supports hybrid inheritance, it can become complex, and care must be taken to avoid issues like the diamond problem, where multiple inheritance paths converge.

class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")

# Next  run
print (" Next  run")