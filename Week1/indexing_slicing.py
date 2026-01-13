str_num = "1230-4567-8902-5739"

# Indexing concept
first_digit = str_num[0]
print(f"The first digit of the string is: {first_digit}")

# Negative indexing concept
last_digit = str_num[-1]
print(f"The last digit of the string is: {last_digit}")
last_second_digit = str_num[-2]
print(f"The second last digit of the string is: {last_second_digit}")

# Slicing concept
""" In the range, the first index is inclusive and the last index is exclusive. 
[0:4] means index 0, 1, 2, and 3. Also [0:4] can be written as [:4] only. Also [5:] means from index 5 to the end of the string."""
first_four_digits = str_num[0:4] 
print(f"The first four digits of the string are: {first_four_digits}")

# Skipping concept
# In the slicing, we can also skip characters by defining a step value
skipped_digits = str_num[::2] # Skipping every second character
print(f"The string after skipping every second character is: {skipped_digits}")

# Reversing concept
reversed_str = str_num[::-1]
print(f"The reversed string is: {reversed_str}")
