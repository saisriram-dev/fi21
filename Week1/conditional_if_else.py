# Conditional expression = A one-line shortcut for an if-else statement
# (sometimes called a ternary operator)

age = int(input("Enter your age: "))
is_adult = True if age >= 18 else False
print("You are eligible to vote." if is_adult else "You are not eligible to vote")
