# Handling multiple exceptions
try:
    result = 10 / 0
except(ZeroDivisionError, TypeError) as e:
    print("Error occurred:", str(e))

#Using the else clause in exception handling


# Next  run
print (" Next  run")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Result is", result)


# Next  run
print (" Next  run")
#Using the finally clause in exception handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("This block of code will always execute.")


# Next  run
print (" Next  run")
#Raising exceptions using raise
try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print("An error occurred:", str(e))


# Next  run
print (" Next  run")
#Creating custom exceptions

class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("An error occurred:", str(e))


# Next  run
print (" Next  run")
# Catching all exceptions using Exception

try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", str(e))
try:
    print(undefined_variable)
except Exception as e:
    print("An error occurred:", str(e))

# Next  run
print (" Next  run")
#Using assert for exception handling
try:
    x = -1
    assert x >= 0, "Only positive values are allowed."
except AssertionError as e:
    print("An error occurred:", str(e))


# Next  run
print (" Next  run")
#Handling exceptions within functions
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None
print(divide(10, 0))



# Next  run
print (" Next  run")
#Using a while loop for handling exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again…")

# Next  run
print (" Next  run")
#Reraising exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught an exception")
#    raise

# Next  run
print (" Next  run")
#Using else clause with try/except inside a function
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    else:
        print("Division successful!")
        return result

print(divide(10, 2))

# Next  run
print (" Next  run")
#Handling exceptions with finally clause in file handling
try:
    f = open('myfile.txt', 'r')
    content = f.read()
    f.close()
except IOError:
    print('File not found.')

# Next  run
print (" Next  run")
4#Ignoring exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    pass

# Next  run
print (" Next  run")
#Propagating exceptions
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    else:
        return x ** 0.5
    
try:
    print(sqrt(-10))
except ValueError as e:
    print("An error occurred:", str(e))


#Example
#Try to open and write to a file that is not writable:
try:
  f = open("example.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")