expense = int(input("Enter your today's total expense: "))
file_path = "C:/Users/P SAI SRI RAM/OneDrive/Desktop/fi21/Week2/Expense Logger/expenses.txt"
with open(file_path, "a") as file:
    file.write(f"\n{expense}")

with open(file_path, "r") as file:
    content = file.read()
    print(content)
