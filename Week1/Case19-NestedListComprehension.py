# list comprehension


numbers = [1, 2, 3, 4]

# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

# next run
print(" Next Run...")

#List Comprehension


numbers = [1, 2, 3, 4, 5]

# create a new list using list comprehension
square_numbers = [num * num for num in numbers]

print(square_numbers)

# Output: [1, 4, 9, 16, 25]

#Conditionals in List Comprehension

# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]


# next run
print(" Next Run...")

#Example: List Comprehension with String

word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)

# Output: ['o']

# next run
print(" Next Run...")

#Nested List Comprehension

multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]

print(multiplication)