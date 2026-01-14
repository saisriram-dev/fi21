# Format specifiers to be used inside f-strings. They are in the form of {value:format_spec}
# We consider the total width of the number including decimal point, digits after decimal point, commas and signs 

price1 = 3234.141
price2 = -8945.56
price3 = 1793.4559

# Using format specifiers to control the number of decimal places
print(f"Price 1 is {price1:.2f}") # .2 means 2 decimal places and f means float
print(f"Price 2 is {price2:.0f}")
print(f"Price 3 is {price3:.1f}")

# Using format specifiers to include commas as thousand separators
print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")

# Combining both decimal places and thousand separators
print(f"Price 1 is {price1:,.2f}")
print(f"Price 2 is {price2:,.0f}")
print(f"Price 3 is {price3:,.1f}")

# Using format specifiers to control width
# Extra width is created by adding spaces before the number
print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10.2f}") # The total width is 10 including decimal point and digits after it.
print(f"Price 3 is {price3:12.3f}") # The total width is 12 including decimal point and digits after it

# Padding zeros instead of spaces
print(f"Price 1 is {price1:010}") # Padding with zeros to make total width 10
print(f"Price 2 is {price2:010.0f}") # Padding with zeros to make total width 10 including the decimal points
print(f"Price 3 is {price3:012.1f}") # Padding with zeros to make total width 12 including the decimal points

# Combining width, decimal places, and thousand separators
print(f"Price 1 is {price1:10,.2f}")
print(f"Price 2 is {price2:10,.0f}")
print(f"Price 3 is {price3:12,.1f}")

# Left aligning the text within the specified width
# Spaces will be added to the right to make total width 10
print(f"Price 1 is {price1:<10}") 
print(f"Price 2 is {price2:<10,.0f}") # Spaces will be added to the right to make total width 10 including commas
print(f"Price 3 is {price3:<12,.1f}")

# Right aligning the text within the specified width
# Spaces will be added to the left to make total width 10
print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:>10,.0f}") # Spaces will be added to the left to make total width 10 including commas
print(f"Price 3 is {price3:>12,.1f}")

# Center aligning the text within the specified width
# Spaces will be added to both sides to make total width 10
print(f"Price 1 is {price1:^10}")
print(f"Price 2 is {price2:^10,.0f}") # Spaces will be added to both sides to make total width 10 including commas
print(f"Price 3 is {price3:^12,.1f}") # Spaces will be added to both sides to make total width 12 including commas

# For positive numbers, a plus sign will be added in front of the number
print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

# For negative numbers, a minus sign will be added in front of the number
print(f"Price 1 is {price1:-}")
print(f"Price 2 is {price2:-}")
print(f"Price 3 is {price3:-}")

# For positive numbers, a space will be added in front of the number
print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")
