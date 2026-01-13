name = input("Enter your name: ")

# To find the length of the name including white spaces. Counting starts from 1.
length = len(name)

# To find the first and last occurrence of an object in a string.
letter = input("Enter a letter to search for in your name: ")
position = name.find(letter)# To find the first occurrence of a letter we want to search for. Indexing starts from 0.
last_position = name.rfind(letter)# To find the last occurrence of a letter we want to search for. Indexing starts from 0.

# To convert the name to uppercase and lowercase.
upper_name = name.upper()
print(upper_name)
lower_name = name.lower()
print(lower_name)

# To capitalize the first letter of the name.
capitalized_name = name.capitalize()
print(name)

# isdigit() method to check if the name contains only digits. Returns only true or false.
is_digit = name.isdigit()
print(is_digit)

# isalpha() method to check if the name contains only alphabets. Returns only false even if a white space is present in the name.
is_alpha = name.isalpha()
print(is_alpha)

# count() and replace() methods
phone_number = input("Enter your phone number: ")
dashe_count = phone_number.count("-")
print(f"The number of dashes in your phone number is: {dashe_count}")

phone_number_1 = phone_number.replace("-", " ")# Replacing dashes with spaces in the phone number.
print(f"Your phone number with spaces instead of dashes is: {phone_number_1}")

phone_number_2 = phone_number.replace("-", "")
print(f"Your phone number without dashes is: {phone_number_2}")

# To demonstrate string concatenation and f-strings.
age = input("Enter your age: ")
print("Hello " + name + ", you are " + age + " years old.")
# Using f-strings for the same output.
print(f"Hello {name}, you are {age} years old.")
