# Function = A block of reusable code

# A simple example without the return statement
def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
# We will get an extra none in the output as the function doesn't have anything to return
print(display_invoice("Joe", 80, "01/01/2026"))

# Positional arguments: They are given in the same order as the parameters in the function
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name('spongebob', 'squarepants')
print(full_name)

# Default arguments = A default value for certain parameters
# They reduce the need of providing more arguments and they are more flexible 
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)
""" If we don't specify the second or third argument for the above function
    it will take default values otherwise it takes the given arguments. 
    Default parameters must be placed after positional parameters. """
print(net_price(500))
print(net_price(500, 0.1)) 

# Keyword arguments
# They increase the redability of the code
def hello(greeting, title, first, last):
    return f"{greeting} {title}{first} {last}"
print(hello("Hello", title="Mr.", last="Squarepants", first="Spongebob"))
""" hello(title="Mr.", first="Spongebob", last="Squarepants", "Hello") returns an error
    as in this case Hello is a positional argument. Order doesn't really matter within  
    keyword arguments. """

# Arbitrary arguments
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
# * It is called as the unpacking operator
# We pack args into a tuple and kwargs into a dictionary
# args example
def disp_name(*args):
    for arg in args:
        print(arg, end=" ")
disp_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
print()

# kwargs example
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print(print_address(street="123 Fake St.", 
              city="Detroit", 
              state="MI", 
              zip="54321"))

# We can also use both *args and **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "street" in kwargs:
        print(f"{kwargs.get('Street')} {kwargs.get('City')}")
    else:
        print(f"{kwargs.get('City')}")
    print(f"{kwargs.get('State')} {kwargs.get('Zip')}")

shipping_label("Spongebob", "Squarepants", "123 Fake St.", 
               City="Detroit", 
               State="MI", 
               Zip="54321")
# We can't switch positional arguments and keyword arguments while calling the function,
# it will output an error
