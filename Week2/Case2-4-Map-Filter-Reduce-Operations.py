#Traditional Code:
persons = ['alfred', 'tabitha', 'william', 'arla']
uppered_persons = []

for person in persons:
    persons_ = person.upper()
    uppered_persons.append(persons_)
    
print(uppered_persons)

# Next  run
print (" Next  run")

# Using the map() function:

persons = ['alfred', 'tabitha', 'william', 'arla']

uppered_persons = list(map(str.upper, persons))

print(uppered_persons)


# Next  run
print (" Next  run")
#An Example utilizing the round() and range() functions:

circle_areas = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)


# Next  run
print (" Next  run")

#filter(), first of all, requires the function to return boolean values (true or false) and then passes each element in the iterable through the function, "filtering" away those that are false.
# Exmaple 1
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]

def is_A_student(score):
    return score > 80
    
passing = list(filter(is_A_student, scores))

print(passing)


# Exmaple 2
myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")

palindromes = list(filter(lambda word: word == word[::-1], myStrings))

print(palindromes)

# Next  run
print (" Next  run")

# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument.

#Example
from functools import reduce

myNumbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second
    
result = reduce(custom_sum, myNumbers)
print(result)



#Example using initial:
from functools import reduce

myNumbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second
    
result = reduce(custom_sum, myNumbers, 10)
print(result)


# Next  run
print (" Next  run")

#Use each of map, filter, and reduce to fix the broken code.

from functools import reduce

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x*x , my_floats))
filter_result = list(filter(lambda name: len(name) < 8, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)

print(map_result)
print(filter_result)
print(reduce_result)


# Next  run
print (" Next  run")
# Function to return double of n
def double(n):
    return n * 2

# Using map to double all numbers
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))

#[10, 12, 14, 16]


# Next  run
print (" Next  run")
import functools

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Use reduce to compute the product of list elements
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)

# Product of list elements: 24


# Next  run
print (" Next  run")

# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))  

#Even numbers: [2, 4, 6, 8, 10]


#Let’s look at an example. Suppose you have a list of integers and you want to double each one:
# Next  run
print (" Next  run")

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)
#[2, 4, 6, 8, 10]

# Next  run
print (" Next  run")
#Another example of using map() is to convert a list of strings to integers:

strings = ["1", "2", "3", "4", "5"]
numbers = list(map(int, strings))
print(numbers)
# [1, 2, 3, 4, 5]

# Next  run
print (" Next  run")
#Let’s look at an example. Suppose you have a list of numbers and you want to filter out the even ones:
numbers = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)
#[1, 3, 5]

# Next  run
print (" Next  run")
#Another example of using filter() is to remove empty strings from a list:
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: len(x) > 0, strings))
print(non_empty)
#['hello', 'world', 'python']

#Let’s look at an example. Suppose you have a list of numbers and you want to calculate their sum using reduce():
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
#15

# Next  run
print (" Next  run")
#Another example of using reduce() is to find the maximum value in a list:
from functools import reduce
numbers = [1, 7, 3, 9, 5]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
#9



# Next  run
print (" Next  run")
#Example 2: Computing statistics
#Suppose you have a list of numbers representing the grades of students in a class, and you want to compute some statistics, such as the mean, median, and standard deviation. Here’s how you could do it using reduce() and some helper functions:
from statistics import mean, median, stdev
grades = [75, 85, 90, 65, 80]
# compute the mean using reduce()
total = reduce(lambda x, y: x + y, grades)
mean_grade = total / len(grades)
print('Mean grade:', mean_grade)
# compute the median using median()
median_grade = median(grades)
print('Median grade:', median_grade)
# compute the standard deviation using stdev()
std_dev = stdev(grades)
print('Standard deviation:', std_dev)
#In this example, we use reduce() to compute the sum of the grades, and then divide by the number of grades to compute the mean. We use median() to compute the median, and `stdev()from thestatistics` module to compute the standard deviation.



# Next  run
print (" Next  run")
#Example 4: Converting data types
#Suppose you have a list of strings representing numbers, and you want to convert them to integers and compute their sum. Here’s how you could do it using map() and reduce():
numbers = ['1', '2', '3', '4', '5']
# convert the strings to integers using map()
integers = map(int, numbers)
# compute the sum using reduce()
total = reduce(lambda x, y: x + y, integers)
print(total)

#In this example, we use map() to convert each string in the list to an integer, and then reduce() to compute their sum.