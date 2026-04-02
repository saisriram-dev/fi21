# A module is a file containing Python definitions and statements. 
# A package is a way of organizing related modules into a single directory hierarchy.

from package_example import APP_NAME, VERSION, DEBUG
from package_example import add, subtract, multiply, divide, power

# If we didn't use __init__.py, we would have to import the modules like this:
# from package_example.config import APP_NAME, VERSION, DEBUG
# from package_example.utils import add, subtract, multiply, divide, power

print(f"App Name: {APP_NAME}")
print(f"Version: {VERSION}")
print(f"Debug: {DEBUG}")

print(add(2, 3))
print(subtract(5, 2))
print(multiply(4, 6))
print(divide(10, 2))
print(power(2, 3))
