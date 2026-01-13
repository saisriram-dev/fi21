# Conditional expression = A one-line shortcut for an if-else statement
# (sometimes called a ternary operator)

# Voting eligibility example
age = int(input("Enter your age: "))
is_adult = True if age >= 18 else False
print("You are eligible to vote." if is_adult else "You are not eligible to vote")

# Grade classification example
score = int(input("Enter your score (0-100): "))
grade = ("A" if score >= 90 else
         "B" if score >= 80 else
         "C" if score >= 70 else
         "D" if score >= 60 else
         "F")
print(f"Your grade is: {grade}")

# Temperature check example
temperature = float(input("Enter the temperature in Celsius: "))
status = "hot" if temperature > 30 else "warm" if temperature >= 20 else "cold"
print(f"The weather is {status}.")

# Number comparison example
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
larger_num = num1 if num1 > num2 else num2
print(f"The larger number is: {larger_num}")

# Even or odd example
number = int(input("Enter a number: "))
parity = "even" if number % 2 == 0 else "odd"
print(f"The number is {parity}.")
