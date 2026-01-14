# Sets
# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() function.
# Sets do not allow duplicate values and do not maintain any specific order.
# Sets are mutable, meaning you can add or remove elements after creation.
# We cannot use indexing or slicing with sets since they are unordered.

# Example: Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set: ", my_set)

# Example: Creating a set using the set() function
another_set = set([4, 5, 6, 7, 8])
print("Another set: ", another_set)

# In operator
if 3 in my_set:
    print("3 is present in my_set")

# Size of the set
print("Size of my_set: ", len(my_set))

# Adding elements to a set
my_set.add(6)
print("Set after adding 6: ", my_set)

# Removing elements from a set
my_set.remove(3)  # Raises KeyError if 3 is not found
print("Set after removing 3: ", my_set)
my_set.discard(10)  # Does not raise an error if 10 is not found
print("Set after discarding 10 (not present): ", my_set)

# Set operations
union_set = my_set.union(another_set) # Union returns all unique elements from both sets
print("Union of sets: ", union_set)

intersection_set = my_set.intersection(another_set) # Intersection returns common elements in both sets
print("Intersection of sets: ", intersection_set)

difference_set = my_set.difference(another_set) # Difference returns elements in my_set but not in another_set
print("Difference of sets (my_set - another_set): ", difference_set)

symmetric_difference_set = my_set.symmetric_difference(another_set) # Symmetric difference returns elements in either set but not in both
print("Symmetric difference of sets: ", symmetric_difference_set)
