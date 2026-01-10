# Arithmetic Operations

# pow function
base = 3
exponent = 4
print(f"{base} raised to the power of {exponent} is {pow(base, exponent)}")

# Floor Division. // does floor division which means that it gives us the step value of the quotient.
num = 3
num //= 2  # num is now 1
print(f"After floor division: {num}")

# round function
num1 = 3.756
num2 = -3.2345
print(f"Rounded value of {num1} is {round(num1)}")
print(f"Rounded value of {num2} is {round(num2)}")
print(f"Rounded value of {num1} to 2 decimal places is {round(num1, 2)}")
print(f"Rounded value of {num2} to 3 decimal places is {round(num2, 3)}")

# Max and Min functions
x = 10
y = 25
print(f"Maximum value between {x} and {y} is {max(x, y)}")
print(f"Minimum value between {x} and {y} is {min(x, y)}")
print(f"Maximum value between 3, 7, 2, 9 is {max(3, 7, 2, 9)}")
print(f"Minimum value between 3, 7, 2, 9 is {min(3, 7, 2, 9)}")

# Addition
num = 3
num += 2  # num is now 5
print(f"After addition: {num}")

# Subtraction
num = 3
num -= 1  # num is now 4
print(f"After subtraction: {num}")

# Multiplication
num = 3
num *= 3  # num is now 9
print(f"After multiplication: {num}")

# Division
num = 3
num /= 4  # num is now 0.75
print(f"After division: {num}")

# Modulus
num = 3
num %= 2  # num is now 1
print(f"After modulus: {num}")

# Exponentiation
num = 3
num **= 3  # num is now 27
print(f"After exponentiation: {num}")

# abs function
num = -5
print(f"Absolute value of {num} is {abs(num)}")
