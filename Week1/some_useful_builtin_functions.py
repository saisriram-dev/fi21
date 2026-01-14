# Lambda functions are small anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression
# They are often used for short, throwaway functions that are not reused elsewhere in the code
# Syntax: lambda arguments: expression
# Example 1: A simple lambda function that adds 10 to the input number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# Example 2: A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# A map function is used to apply a function to all items in an iterable (like a list) and returns a map object (which is an iterator)
# Syntax: map(function, iterable)
# Example: Using a lambda function with map to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Filter function is used to filter items in an iterable based on a function that returns True or False
# Syntax: filter(function, iterable)
n = int(input("Enter a number to filter even numbers up to that number: "))
nums = [i for i in range(1, n + 1)]
print(nums)  # Output: List of numbers from 1 to n
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: List of even numbers up to n

# .split() is a built-in string method that splits a string into a list of substrings based on a specified delimiter (default is whitespace)
# Syntax: string.split(separator, maxsplit)
# Example: Splitting a sentence into words
sentence = "This is an example sentence."
words = sentence.split() # By default, splits by whitespace
print(words)  # Output: ['This', 'is', 'an', 'example', 'sentence.']

# Example: Splitting a string by a specific delimiter
data = "apple,banana,cherry,date"
fruits = data.split(",")  # Splits by comma
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# .join() is a built-in string method that joins elements of an iterable (like a list) into a single string, with a specified separator
# Syntax: separator.join(iterable)
# Example: Joining a list of words into a single string with spaces
words_list = ['Hello', 'world', 'this', 'is', 'Python']
joined_string = ' '.join(words_list)
print(joined_string)  # Output: "Hello world this is Python"

# Example: Joining a list of items with a comma separator
items = ['apple', 'banana', 'cherry']
joined_items = ', '.join(items)
print(joined_items)  # Output: "apple, banana, cherry"

# range() is a built-in function that generates a sequence of numbers within a specified range
# Syntax: range(start, stop, step)
# Example 1: Generating numbers from 0 to 4
for i in range(5):
    print(i, end=' ')  # Output: 0 1 2 3 4
print()  # For newline

# Example 2: Generating numbers from 2 to 10 with a step of 2
for i in range(2, 11, 2):
    print(i, end=' ')  # Output: 2 4 6 8 10
print()  # For newline

# Example 3: Generating numbers in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i, end=' ')  # Output: 10 9 8 7 6 5 4 3 2 1
print()  # For newline

# enumerate() is a built-in function that adds a counter to an iterable and returns it as an enumerate object
# Syntax: enumerate(iterable, start=0)
# Example: Using enumerate to get index and value from a list
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# zip() is a built-in function that combines multiple iterables (like lists or tuples) into a single iterable of tuples
# Syntax: zip(iterable1, iterable2, ...)
# Example: Zipping two lists together
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# Example: Zipping three lists together
cities = ['New York', 'Los Angeles', 'Chicago']
combined_info = list(zip(names, ages, cities))
print(combined_info)  # Output: [('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 35, 'Chicago')]
