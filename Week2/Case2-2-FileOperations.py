fileNameWithFullURL = 'c:\\Users\\HP\\Documents\\GitHub\\AI-ML-Explorer\\Week2\\example.txt'
FullURL= 'c:\\Users\\HP\\Documents\\GitHub\\AI-ML-Explorer\\Week2\\'
#Let’s create a file called “example.txt” with some text in it. Save the file in the same folder as that of the Python file. We will try to read this text file using Python.
file = open(fileNameWithFullURL, 'r')
content = file.read()
print(content)
file.close()


# Next  run
print (" Next  run")
# Writing to a file
with open(fileNameWithFullURL, 'w') as file:
    file.write("Hello, Pythonista!")

# Next  run
print (" Next  run")
#Reading a specific number of characters
with open(fileNameWithFullURL, 'r') as file:
    print(file.read(5))

# Next  run
print (" Next  run")
#Reading one line at a time using readline
with open(fileNameWithFullURL, 'r') as file:
  print(file.readline())


# Next  run
print (" Next  run")
#Reading all lines at once using readlines
with open(fileNameWithFullURL, 'r') as file:
    print(file.readlines())

# Next  run
print (" Next  run")
#Looping over a file object
with open(fileNameWithFullURL, 'r') as file:
    for line in file:
        print(line, end='')

# Next  run
print (" Next  run")
#Writing multiple lines to a file
lines = ["Hello, Pythonista!\n", "Welcome to the world of Python.\n"]
with open(fileNameWithFullURL, 'w') as file:
    file.writelines(lines)

# Next  run
print (" Next  run")
# Appending to a file
with open(fileNameWithFullURL, 'a') as file:
    file.write("\nKeep on learning!")


# Next  run
print (" Next  run")
#Using tell to get the current file position
with open(fileNameWithFullURL, 'r') as file:
    file.read(10)
    print(file.tell())

# Next  run
print (" Next  run")
#Using seek to change the file position
with open(fileNameWithFullURL, 'r') as file:
    file.seek(15)
    print(file.read())

# Next  run
print (" Next  run")
#Checking if a file exists
import os
print(os.path.isfile(fileNameWithFullURL))

# Next  run
print (" Next  run")
#Getting the size of a file
import os
print(os.path.getsize(fileNameWithFullURL))


# Next  run
print (" Next  run")
#Getting the size of a file
import os
os.rename(fileNameWithFullURL, FullURL+'new_example.txt')

# Next  run
print (" Next  run")
#Getting the size of a file
import os
os.remove(FullURL+'new_example.txt')

# Next  run
print (" Next  run")
#Creating a directory
import os
os.mkdir(FullURL+'newDirectory')


# Next  run
print (" Next  run")
#Changing the current working directory + Getting the current working directory
import os
os.chdir(FullURL+'newDirectory')
print(os.getcwd())

# Next  run
print (" Next  run")
#Listing all files and directories
import os
print(os.listdir())

# Next  run
print (" Next  run")
#Removing a directory
import os
os.rmdir(FullURL+'newDirectory')

