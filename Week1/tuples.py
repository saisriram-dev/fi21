# Tuples
# Tuples are immutable sequences in Python, meaning their elements cannot be changed after creation.
# Note: Since tuples are immutable, operations like adding, removing, or changing elements are not allowed and will raise errors if attempted.
# They are defined using parentheses () and can contain elements of different data types.
# Tuples allow duplicate elements in them, meaning the same value can appear multiple times.
# They are faster than lists. We try to use tuples when we have a collection of items that should not change throughout the program.

# Example: Creating a tuple
my_tuple = (1, "hello", 3.14, True, "hello")
print("Initial tuple: ", my_tuple)

# Indexing
first_element = my_tuple[0]
last_element = my_tuple[-1]
print("First element: ", first_element)
print("Last element: ", last_element)

# Slicing
slice_tuple = my_tuple[1:4]
print("Sliced tuple: ", slice_tuple)

# Iteration
for element in my_tuple:
    print(element)

# Length
print("Total number of elements in tuple:", len(my_tuple))

# In operator
if "hello" in my_tuple: # As "hello" is present in the tuple the condition becomes true.
    print("'hello' is in the tuple!")

# Count occurrences
count_of_hello = my_tuple.count("hello")
print("Count of 'hello': ", count_of_hello)

# Index of element
index_of_pi = my_tuple.index(3.14)
print("Index of 3.14: ", index_of_pi)

# my_tuple[0] = 10 # This will raise a TypeError since tuples are immutable
# my_tuple.append(5) # This will raise an AttributeError since tuples do not have an append method
# my_tuple.remove("hello") # This will raise an AttributeError since tuples do not have a remove method
# my_tuple.pop() # This will raise an AttributeError since tuples do not have a pop method
# my_tuple.insert(1, "new") # This will raise an AttributeError since tuples do not have an insert method
# my_tuple.extend((6, 7)) # This will raise an AttributeError since tuples do not have an extend method
# my_tuple.sort() # This will raise an AttributeError since tuples do not have a sort method
# my_tuple.reverse() # This will raise an AttributeError since tuples do not have a reverse
# my_tuple.clear() # This will raise an AttributeError since tuples do not have a clear method
