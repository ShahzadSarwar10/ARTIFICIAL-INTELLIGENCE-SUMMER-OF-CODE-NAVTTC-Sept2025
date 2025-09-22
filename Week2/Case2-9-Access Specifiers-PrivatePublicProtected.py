#Access Specifiers: Private, Public, Protected

"""Public Access Modifier
The public access modifier allows class members to be accessible anywhere in the program. By default, all members in a Python class are public unless explicitly specified otherwise."""
class MyClass:
    def __init__(self):
        self.my_public_attribute = "I am a public attribute"

    def my_public_method(self):
        print("I am a public method")

# Accessing public members
obj = MyClass()
print(obj.my_public_attribute)
obj.my_public_method()


"""I am a public attribute
I am a public method"""


#Example 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Accessing public members
rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()

#15


#Protected Access Modifier
#The protected access modifier restricts the access of class members within the class and its subclasses. To denote a member as protected, you can prefix it conventionally with a single underscore (_).

class MyBaseClass:
    def __init__(self):
        self._my_protected_attribute = "I am a protected attribute"

    def _my_protected_method(self):
        print("I am a protected method")

class MyDerivedClass(MyBaseClass):
    def __init__(self):
        super().__init__()

    def access_protected_member(self):
        print(self._my_protected_attribute)
        self._my_protected_method()

# Accessing protected members
obj = MyDerivedClass()
obj.access_protected_member()

"""I am a protected attribute
I am a protected method"""


#Example 2
class Animal:
    def __init__(self, name):
        self._name = name

    def _make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self._name} barks")
        self._make_sound()
# Accessing protected members
dog = Dog("Buddy")
dog.make_sound()

#Buddy barks

#Private Access Modifier
#The private access modifier restricts the access of class members to within the class only. To denote a member as private, you can prefix it conventionally with double underscores (__).

class MyClass:
    def __init__(self):
        self.__my_private_attribute = "I am a private attribute"

    def __my_private_method(self):
        print("I am a private method")

# Accessing private members (will result in AttributeError)
obj = MyClass()
# print(obj.__my_private_attribute)
# obj.__my_private_method()

# Attempting to access private members will result in an AttributeError


#Example 2
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def introduce(self):
        self.__display_info()

# Accessing private members
person = Person("Alice", 30)
person.introduce()


#Name: Alice, Age: 30

""""Conclusion
Public Access Modifier makes members accessible anywhere in the program without restrictions.
Protected Access Modifier restricts access within the class and its subclasses, denoted by a single underscore.
Private Access Modifier confines access to within the class only, indicated by a double underscore.
Access modifiers are essential tools for managing the visibility and accessibility of class members in Python.
Access modifiers help encapsulate and protect a class's internal state."""