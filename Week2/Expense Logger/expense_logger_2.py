from pathlib import Path

# Creating and storing the required paths for future access using the pathlib module
base = Path(input("Enter the path address where you want to store your expenses list: "))
expenses_file = base/"expenses.txt"
expenses_file.touch(exist_ok=True) # Created the expenses.txt folder

# Creating the required variables
total_spending = 0
num_lines = 0
expenses=[]
dates=[]

while True:
    date = input("Enter the date in the format dd-mm-yyyy: ")
    try:
        amount = int(input("Enter your expenses for the above particular date: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    else: 
        print("Expenses saved successfully!")

    # Updating the expenses and dates lists
    dates.append(date)
    expenses.append(amount)
    
    # Designing the flow of the program
    permission = input("Do you want to continue (y/n): ")
    if permission.lower() == "n":
        break
    else:
        continue

# Updating the expenses.txt file
with open(expenses_file, "a") as file:
    for i in range(len(expenses)):
        file.write(dates[i] + ", " + str(expenses[i]) + "\n")

# This is for reading the expenses.txt file
with open(expenses_file, "r") as file:
    for line in file:
        # .partition() splits the line into three parts and returns them as a tuple
        # (Before the separator, the separator, and after the separator)
        # Even if the separator is not found, the tuple will still have three elements
        # The first element will be the line itself, the second and third elements will be empty
        total_spending += int(line.partition(", ")[2])
        num_lines += 1
    average_spending = total_spending / num_lines
        

print(f"Your total spending so far is: ₹{total_spending}")
print(f"Your average expenses is: ₹{average_spending}")
