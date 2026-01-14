# While loop = Execute some code repeatedly while a condition is true

# A simple example of a while loop which prompts users to enter their name
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")
print(name)

print(f"Hello, {name}!")

# A break statement example to exit the loop when a condition is met
num = int(input("Enter a positive number: "))
while True:
    if num < 0:
        print("The number is negative. Please enter a positive number.")
        num = int(input("Enter a positive number: "))
    else:
        break
print(f"You entered the positive number: {num}")

# An infinite loop example (uncomment to run)
# while True:
#     print("This is an infinite loop!")

# Another infinite loop example (Uncomment to run and only runs infinitely if no name is entered)
# name = input("Enter your name: ")
# while name == "":
#    print("You did not enter your name!")
