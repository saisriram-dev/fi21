# Lists
# Lists are ordered. We can access elements by their index.
# Lists are mutable, meaning we can change their content. Add, remove, or modify elements.
# Lists can contain elements of different data types, including other lists.
# Lists allow duplicate elements in them, meaning the same value can appear multiple times.

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Indexing
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("First fruit: ", first_fruit)
print("Last fruit: ", last_fruit)

# Slicing
citrus_fruits = fruits[1:4]
print("Citrus fruits slice:", citrus_fruits)

# Iteration
for fruit in fruits:
    print(fruit)

# Length
print("Total number of fruits:", len(fruits))

# In operator
if "banana" in fruits: # As banana is present in the fruits list the condition becomes true.
    print("Banana is in the list!")

# Appending
fruits.append("honeydew")
print(fruits)

# Removing
fruits.remove("fig")
print(fruits)

# Changing elements
fruits[2] = "cantaloupe"
print(fruits)

# Pop element
popped_fruit = fruits.pop()
print(fruits)

# Insert element
fruits.insert(1, "blueberry")
print(fruits)

# Extend list
more_fruits = ["kiwi", "lemon"]
final_fruits = fruits.extend(more_fruits)
# The 'final_fruits' list gets assigned the value 'None'.
# And the 'fruits' list gets extended with the 'more_fruits' list.
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Index of element
index_of_date = fruits.index("date")
print("Index of date: ", index_of_date)

# Count occurrences
count_of_banana = fruits.count("banana")
count_of_honeydew = fruits.count("honeydew") # Honewdew was popped earlier, so count will be 0
print("Count of banana: ", count_of_banana)
print("Count of honeydew: ", count_of_honeydew)

# Clear list
fruits.clear()
print(fruits)
