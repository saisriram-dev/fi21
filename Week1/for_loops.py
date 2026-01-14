# For loops in Python are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects

# Example: Iterating over a range of numbers 
for x in range(1, 6): # This will iterate from 1 to 5 as the upper limit is exclusive
    print(x)
print("Finished iterating over range(5).")

# For not creating a new line after each print statement
for x in range(1, 6):
    print(x, end=' ') # end=' ' will add a space instead of a new line after each print
print("\nFinished iterating over range(5) with space separation.")

# Reversed range example
for y in range(5, 0, -1): # Here 0 is exclusive, so it will print from 5 to 1 and -1 is the step value
    print(y)
print("Finished iterating over reversed range(5).")
for x in reversed(range(1, 6)): # Another way to iterate in reverse order
    print(x)
print("Finished iterating over reversed range(5).")

# Example: Even numbers from 0 to 10
for i in range(0, 11, 2): # This will iterate from 0 to 10 with a step of 2
    print(i)
print("Finished iterating over even numbers from 0 to 10.")

# Example: Iterating over a string
credit_card = "1234-5678-9012-3456"
for digit in credit_card:
    print(digit)
print("Finished iterating over credit card digits.")

# Break statement example
for num in range(1, 11):
    if num == 6:
        break # Exit the loop when num is 6
    print(num)
print("Loop exited using break statement.")

# Continue statement example
for num in range(1, 11):
    if num % 2 == 0:
        continue # Skip even numbers
    print(num)
print("Finished iterating and skipping even numbers.")

# Nested for loop example
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()  # Move to the next line after each row
print("Finished printing the grid.")
