file_path = "C:/Users/P SAI SRI RAM/OneDrive/Desktop/fi21/Week2/Expense Logger/expenses.txt"

""" Initial program """
# expense = int(input("Enter your today's total expense: "))
# with open(file_path, "a") as file:
#     file.write(f"\n{expense}")

# with open(file_path, "r") as file:
#     content = file.read()
#     print(content)

with open(file_path, "r") as file:
    lines = [line.rstrip("\n") for line in file.readlines()] # file.readlines() gives a list as output
    lines = [int(line) for line in lines] # Converting each item in the list to integer type
    print(lines)

    total_expense = sum(lines)
    average_expense = total_expense / len(lines)
    print(f"Total expense: {total_expense}")
    print(f"Average expense: {average_expense}")