# Typecasting is the process of converting a variablr from one data type to another data type.

"""For any program including numbers, it is recommended to mainly use the float data type unless mentioned to use integer
   data type specifically. This is because float can handle both whole numbers and decimal numbers, 
   whereas integer can only handle whole numbers. So it may convert decimal numbers to whole numbers by removing the decimal 
   part which may lead to loss of data.
"""

# Variables
name = "John"
age = 16
weight = 49.6
is_student = True

# To know the type of variable we use type() function
print(type(name))
print(type(age))
print(type(weight))
print(type(is_student))

# Typecasting examples
empty = ""          # An empty string
empty = bool(empty)  # Converting empty string to boolean
print(empty) # Prints False since the string is empty

age = str(age)          # Converting integer to string. We can't do mathematical operations on the age variable from now on.
print(type(age))

weight = int(weight)   # Converting float to integer
print(type(weight))

is_student = str(is_student)  # Converting boolean to string
print(type(is_student))

weight = float(weight)  # Converting integer to float
print(type(weight))

name = bool(name)     # Converting string to boolean
print(name)
