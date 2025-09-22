#Another class example
# Next  run
print (" Next  run")
class Employee:
   "Common base class for all employees"
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


"""Name :  Zara , Salary:  2000
Name :  Manni , Salary:  5000
Total Employee 2"""

# Add an 'age' attribute
emp1.age = 7  
# Modify 'age' attribute
emp1.age = 8  
# Delete 'age' attribute
#del emp1.age  

"""Instead of using the normal statements to access attributes, you can also use the following functions −

getattr(obj, name[, default]) − to access the attribute of object.

hasattr(obj,name) − to check if an attribute exists or not.

setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

delattr(obj, name) − to delete an attribute."""

# Returns true if 'age' attribute exists
print(hasattr(emp1, 'age'))
# Returns value of 'age' attribute
print(getattr(emp1, 'age'))    
# Set attribute 'age' at 9
setattr(emp1, 'age', 9) 
print(emp1.age)
# Delete attribute 'age'
delattr(emp1, 'age')


"""Built-In Class Attributes in Python
Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

SNo.	Attributes & Description
1	__dict__
Dictionary containing the class's namespace.

2	__doc__
Class documentation string or none, if undefined.

3	__name__
Class name

4	__module__
Module name in which the class is defined. This attribute is "__main__" in interactive mode.

5	__bases__
A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list."""


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

