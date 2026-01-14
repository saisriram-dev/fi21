# 2D lists (Lists of Lists)
# A 2D list is essentially a list where each element is itself a list. This allows us to create a grid-like structure.

# Example: Creating a 2D list to represent a grocery list
fruits     = ["apple", "banana", "cherry", "date"]
vegetables = ["asparagus", "broccoli", "carrot", "daikon"]
meats      = ["beef", "chicken", "pork", "lamb"]
groceries = [fruits, vegetables, meats] # groceries[0] is the fruits list, groceries[1] is the vegetables listand so on.
print(groceries) # Output: [['apple', 'banana', 'cherry', 'date'], ['asparagus', 'broccoli', 'carrot', 'daikon'], ['beef', 'chicken', 'pork', 'lamb']]

# Accessing elements in a 2D list
print(groceries[0][1]) # Output: banana (Accessing the second fruit)
print(groceries[1][2]) # Output: carrot (Accessing the third vegetable)
print(groceries[2][0]) # Output: beef (Accessing the first meat

# Example: Creating a 2D list (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the matrix
print(matrix[0][0]) # Output: 1 (First row, first column)
print(matrix[1][2]) # Output: 6 (Second row, third column)
print(matrix[2][1]) # Output: 8 (Third row, second column)

# Iterating through a 2D list
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # For a new line after each row

# Modifying elements in a 2D list
matrix[0][0] = 10 # Changing the first element from 1 to 10
print(matrix) # Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# We can even create a list of tuples or a list of sets, but those are less common for 2D structures.
# And we can also create tuple of tuples or set of sets, but those are even less common for 2D structures.
