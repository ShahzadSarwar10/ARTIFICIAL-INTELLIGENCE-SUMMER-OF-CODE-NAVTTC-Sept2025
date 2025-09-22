# Positional vs keyword arguments
#When you call the built-in print function, you can pass in any number of arguments positionally. We're passing in four positional arguments here:
print(2, 1, 3, 4)
#2 1 3 4

#Keyword arguments (a.k.a. named arguments)
#The print function also accepts some arguments as keyword arguments.
#The print function accepts an optional sep argument (which defaults to a space character).
print(2, 1, 3, 4, sep=' ')
#2 1 3 4
print(2, 1, 3, 4)
#2 1 3 4
print(2, 1, 3, 4, sep='-')
#2-1-3-4
print(2, 1, 3, 4, sep=', ')
#2, 1, 3, 4

#There's also an optional end keyword argument. The end argument defaults to a newline character:
print(2, 1, 3, 4, sep=', ', end='\n')
#2, 1, 3, 4

#But we can put some exclamation marks in the end argument (before a newline) to print out exclamation marks at the end:
print(2, 1, 3, 4, sep=', ', end='!!\n')
#2, 1, 3, 4!!


#The order of keyword arguments doesn't matter
#The order of the print function's sep and end arguments doesn't actually matter.
print(2, 1, 3, 4, end='!!\n', sep=', ')
#2, 1, 3, 4!!

#For example, the built-in sum function accepts a first argument:
sum([2, 1, 3 ,4])
#10

#But it also accepts a second argument, which defaults to zero:
sum([2, 1, 3 ,4], 0)
#10

#If we change that second argument to 1, we'll see that this is the start value for the returned summation:
sum([2, 1, 3 ,4], 1)
#11

#We're passing in one positional argument and one keyword argument.'
sum([2, 1, 3 ,4], start=1)
#11

# Next  run
print (" Next  run")
############# NextExamples
#Positional-Only Arguments - Position-only arguments mean whenever we pass the arguments in the order we have defined function parameters in which if you change the argument position then you may get the unexpected output. We should use positional Arguments whenever we know the order of argument to be passed. 
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

nameAge(name="Prince", age=20)

nameAge(age=20, name="Prince")

#Hi, I am Prince
#My age is  20
#Hi, I am Prince
#My age is  20

#During the function call, we have used the Position such that the first argument(or value) will be assigned to name and the second argument(or value) will be assigned to age. By changing the position or in case you forgot the order of the position then the values can be used at the wrong places as we can see in the below example of Case-2 that 20 has been assigned to the name and Prince has been assigned to age.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# You will get correct output because argument is given in order
print("Case-1:")
nameAge("Prince", 20)
# You will get incorrect output because argument is not in order
print("\nCase-2:")
nameAge(20, "Prince")


#Case-1:
#Hi, I am Prince
#My age is  20

#Case-2:
#Hi, I am 20
#My age is  Prince


# Next  run
print (" Next  run")
#Example 2
#During the calling of the function, we have used the position to pass the argument(or value) such that first value will be assigned to a and second value will be assigned to b. But in the result2 you will getting the incorrect output because in the function declaration b should be subtracted from the a but in result2 a is been subtracted from b because of the swapped position.

def minus(a, b):
    return a - b


a, b = 20, 10
result1 = minus(a, b)
print("Used Positional arguments:", result1)

# you will get incorrect output because
# expected was (a-b) but you will be getting (b-a)
# because of swapped position of value a and b

result2 = minus(b, a)
print("Used Positional arguments:", result2)

#Used Positional arguments: 10
#Used Positional arguments: -10

# Next  run
print (" Next  run")

#Positional-Only Arguments in Python
def greet_person(person, repeat):
    print(f"Hello {person}, how are you doing today?\n" * repeat)
# 1.
greet_person("Zahra", 2)
# 2.
greet_person("Zahra", repeat=2)
# 3.
greet_person(person="Zahra", repeat=2)


# Next  run
print (" Next  run")

#Positional-Only And Keyword-Only Arguments in Python
#The part of the function signature which leads to this error is the asterisk *. Any parameter after the asterisk * must be matched to a keyword-only argument. Therefore the arguments "James" and "Claire" lead to this error. This function can take at most two positional arguments, as mentioned in the error message:
#When you define a function, you can force the user to use positional-only arguments for some of the arguments: You can add a forward slash / as one of the parameters in the function definition All arguments assigned to parameters before the / must be positional arguments

def greet(greeting, /, repeat, *, host, guest):
    for _ in range(repeat):
        print(f"{host} says '{greeting}' to {guest}")
# 1.
#greet("Hello!", 3, "James", "Claire")
# 2.
greet("Hello!", 3, host="James", guest="Claire")
# 3.
greet("Hello!", repeat=3, host="James", guest="Claire")
# 4.
#greet(greeting="Hello", repeat=3, host="James", guest="Claire")


# Next  run
print (" Next  run")
# Version without an *
def greetV2(greeting, /, repeat, host, guest):
    for _ in range(repeat):
        print(f"{host} says '{greeting}' to {guest}")
# 1. (no asterisk in signature)
greetV2("Hello!", 3, "James", "Claire")

# Next  run
print (" Next  run")

def greetV3(*, host, guest):
    print(f"{host} says hello to {guest}")
# 3.
greetV3(guest="Claire", host="James")


# Next  run
print (" Next  run")

#Positional-Only Arguments 
#Positional-only arguments can only be passed by position, not by keyword. This is useful when you want to ensure that certain arguments are always passed in a specific order. 
#You can define positional-only arguments using a / in the function signature. Everything before the / is positional-only. 

def example(pos1, pos2, /, pos_or_kw, *, kw1, kw2): 
    print(f"pos1: {pos1}, pos2: {pos2}, pos_or_kw: {pos_or_kw}, kw1: {kw1}, kw2: {kw2}") 

# Correct usage 
example(1, 2, 3, kw1=4, kw2=5) 

# Incorrect usage 
example(pos1=1, pos2=2, pos_or_kw=3, kw1=4, kw2=5)  # Raises TypeError 


# Next  run
print (" Next  run")
#Keyword-Only Arguments 
#Keyword-only arguments must be passed by keyword, not by position. This is useful when you want to make sure that certain arguments are always explicitly named, which can improve code readability. 
#You can define keyword-only arguments using a * in the function signature. Everything after the * is keyword-only. 
def exampleV2(pos1, pos2, *, kw1, kw2): 
    print(f"pos1: {pos1}, pos2: {pos2}, kw1: {kw1}, kw2: {kw2}") 

# Correct usage 
exampleV2(1, 2, kw1=3, kw2=4) 

# Incorrect usage 
exampleV2(1, 2, 3, 4)  # Raises TypeError 

# Next  run
print (" Next  run")

#Combining Both 
#You can combine both positional-only and keyword-only arguments in a single function definition to have fine-grained control over how arguments are passed. 

def exampleV3(pos1, pos2, /, pos_or_kw, *, kw1, kw2): 
    print(f"pos1: {pos1}, pos2: {pos2}, pos_or_kw: {pos_or_kw}, kw1: {kw1}, kw2: {kw2}") 

  
# Correct usage 
exampleV3(1, 2, 3, kw1=4, kw2=5) 

# Incorrect usage 
exampleV3(pos1=1, pos2=2, pos_or_kw=3, kw1=4, kw2=5)  # Raises TypeError 

#Summary 
#Positional-Only Arguments: Defined before /, must be passed by position. 
#Keyword-Only Arguments: Defined after *, must be passed by keyword. 
#I hope this helps clarify the differences! If you have any more questions or need further examples, feel free to ask. 