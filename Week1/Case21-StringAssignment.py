#Asignment # 1
#Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)



#Asignment # 2
#Write a program to count occurrences of all characters within a string
str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)
 
#Asignment # 3
#Reverse a given string

# Solution 1
text = 'abcde'
length = len(text)
text_rev = ""
while length>0:
   text_rev += text[length-1]
   length = length-1

print(text_rev)

# Solution 2
str1 = "PYnative"
print("Original String is:", str1)

str1 = str1[::-1]
print("Reversed String is:", str1)


# Solution 2

str1 = "PYnative"
print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)

#Asignment # 4
#Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)


#Asignment # 5
#Solution 1: Use string functions translate() and maketrans().
#The string.punctuation constant contain all special symbols.
#Remove special symbols / punctuation from a string
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)