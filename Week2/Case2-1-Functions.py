#Create a Function
def greet():
    print('Hello World!')

# Function Call
greet()



# Next  run
print (" Next  run")
# Example: Function to Add Two Numbers
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)


# Next  run
print (" Next  run")
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)

# Next  run
print (" Next  run")
def future_function():
    pass

# this will execute without any action or error
future_function() 


# Next  run
print (" Next  run")
# Example: Python Library Function
import math

# sqrt computes the square root
square_root = math.sqrt(3)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)


# Next  run
print (" Next  run")
# Note that the order of parameters does not matter.
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

# Next  run
print (" Next  run")
#it prints default age if it is not passed −
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# Next  run
print (" Next  run")
#Positional-only arguments
#Those arguments that can only be specified by their position in the function call is called as Positional-only arguments. They are defined by placing a "/" in the function's parameter list after all positional-only parameters. This feature was introduced with the release of Python 3.8.
def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11) 

# Next  run
print (" Next  run")
#Keyword-only arguments
#Those arguments that must be specified by their name while calling the function is known as Keyword-only arguments. They are defined by placing an asterisk ("*") in the function's parameter list before any keyword-only parameters. This type of argument can only be passed to a function as a keyword argument, not a positional argument.
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 

# Next  run
print (" Next  run")
#Arbitrary or Variable-length Arguments
#You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

#
#Output is:
#10
#Output is:
#70
#60
#50

# Next  run
print (" Next  run")
def add(x,y):
   z=x+y
   return z
a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))

# Next  run
print (" Next  run")
#The Anonymous Functions
#The functions are called anonymous when they are not declared in the standard manner by using the def keyword. Instead, they are defined using the lambda keyword.

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

# Next  run
print (" Next  run")
#Global vs. Local variables
#Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.

total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total) 

# Next  run
print (" Next  run")
#Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Next  run
print (" Next  run")
#Let's create a simple function cube() that returns the volume and total surface area of a cube, given the length of its side.

def cube(side):
  volume = side **3
  surface_area = 6 * (side**2)
  return volume, surface_area

returned_values = cube(8)
print(returned_values)

# Output
(512, 384)

# Next  run
print (" Next  run")
#How to Create a Function that Takes a Variable Number of Arguments in Python

def my_var_sum(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum


# Example 1 with 4 numbers
sum = my_var_sum(99,10,54,23)
print(f"The numbers that you have add up to {sum}")
# Output
#The numbers that you have add up to 186

# Example 2 with 3 numbers
sum = my_var_sum(9,87,45)
print(f"The numbers that you have add up to {sum}")
# Output
#The numbers that you have add up to 141

# Example 3 with 6 numbers
sum = my_var_sum(5,21,36,79,45,65)
print(f"The numbers that you have add up to {sum}")
# Output
#The numbers that you have add up to 251


# Next  run
print (" Next  run")
#Python function that returns a dictionary

def myAnimals(a1,a2,a3):
    Animalgroup = {'Kitten':a1,'Puppy':a2,'Pup':a3}
    return Animalgroup

output = myAnimals("Cat","Dog","Rat")
print(output)

# Next  run
print (" Next  run")
#Python function that returns a tuple

def myVeggies(v1,v2,v3):
    vegtuple = (v1,v2,v3)
    return vegtuple

output = myVeggies("Carrot","Potato","Tomato")
print(output)

# Next  run
print (" Next  run")


def SwapTwoNumbers(a,b):
    print("Before Swap: ",a,b)
    a = a+b
    b = a-b
    a = a-b
    return a,b
    
a,b = SwapTwoNumbers(17,24)
print("After Swap: ",a,b)


#Inner Function
# Next  run
print (" Next  run")
def function1():
    p ="Hello Pythonista" 
    def function2():
        print(p)
    function2()
    
function1()

#optinal parameter example
# Next  run
print (" Next  run")
def Calendar(year,month,date=''):
    print(year,month,date)
    
Calendar(2023,2)

Calendar(2023,2,14)


# Python function to check if a number is palindrome or not
# Next  run
print (" Next  run")
def palindromeCheck(num):
    temp = num
    rev = 0
    while(num != 0):
        r = num%10
        rev = rev*10+r
        num = num//10
    if(rev == temp):
        print(temp, "is a palindrome number")
    else:
        print(temp, "is not a palindrome number")
    

palindromeCheck(131)
palindromeCheck(34)


# Python function to find the factorial of a number
# Next  run
print (" Next  run")
def factorial(n):
    fact = 1
    while(n!=0):
        fact *= n 
        n = n-1
    print("The factorial is",fact)
    
inputNumber = int(input("Enter the number: "))
factorial(inputNumber)


#Inner function
# Next  run
print (" Next  run")
def greeting(first, last):
  # nested helper function
  def getFullName():
    return first + " " + last

  print("Hi, " + getFullName() + "!")

greeting('Quincy', 'Larson')

#Hi, Quincy Larson!


# Next  run
print (" Next  run")
#
# 

#Pass by Value and Pass by Reference in Python
#Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 
#Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

def call_by_value(x):
    x = x * 2
    print("in function value updated to", x)
    return

def call_by_reference(list):
    list.append("D")
    print("in function list updated to", list)
    return

my_list = ["E"]
num = 6
print("number before=", num)
call_by_value(num)
print("after function num value=", num)
print("list before",my_list)
call_by_reference(my_list)
print("after function list is ",my_list)


#number before= 6
#in function value updated to 12
#after function num value= 6
#list before ['E']
#in function list updated to ['E', 'D']
#after function list is  ['E', 'D']


# Next  run
print (" Next  run")
#Local variables exist inside a function and cannot be accessed outside it.
#Global variables exist throughout the script, but modifying them inside a function requires the global keyword.
#Nonlocal variables allow modifying a variable from an enclosing function using the nonlocal keyword.


x = 10  # Global variable

def modify_global():
    global x
    x = 20  # Modifies the global variable

modify_global()
print(x)  # Output: 20



def outer_function():
    y = 10  # Enclosing scope variable

    def inner_function():
        nonlocal y
        y = 20  # Modifies the enclosing scope variable

    inner_function()
    print(y)  # Output: 20

outer_function()


# Next  run
print (" Next  run")
def fun1(): # outer function
    a = 45
    
    def fun2(): # inner function
        nonlocal a  # allows modification of `a` from fun1
        a=54
        print(a)
    
    fun2()
    print(a)

fun1()

#Output
#54
#54
