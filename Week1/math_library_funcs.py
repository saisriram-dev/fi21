import math

# Square root function
num = 49
print(math.sqrt(num))

# Power function    
base = 5
exp = 3
print(pow(5, 3))

# Floor function
num = 7.9
print(math.floor(num))

# Ceil function
num = 6.9
print(math.ceil(num))

# Factorial function
num = 5
print(math.factorial(num))

# Pi Value
print(math.pi)

# Napier's Constant
print(math.e)

# Natural logarithm function [Logarithm function with base e(ln function) ~ 2.71828]
napc = math.e
print(math.log(napc))

# Logarithm function with base 10
num = 1000
print(math.log10(num))

# Logarithm function with base 2
num = 16
print(math.log2(num))

# Sine function
angle = math.pi / 2  # 90 degrees in radians
print(math.sin(angle)) # Angle must be in radians

# Tangent function
angle = math.pi / 4  # 45 degrees in radians
print(math.tan(angle))

# Cosine function
print(math.cos(math.pi/2)) # Output is 6.123233995736766e-17 which is extremely close to 0 due to floating point precision limitations

# Inverse Sine function
value = 1
print(math.asin(value))  # Output is in radians

# Inverse Cosine function
value = 0
print(math.acos(value))  # Output is in radians

# Inverse Tangent function
value = 1
print(math.atan(value))  # Output is in radians

# Hyperbolic Sine function
value = 0
print(math.sinh(value))

# Hyperbolic Cosine function
value = 0
print(math.cosh(value))

# Hyperbolic Tangent function
value = 0
print(math.tanh(value))

# Degrees to Radians conversion
degrees = 180
print(math.radians(degrees)) # Use radians function, input must be degrees then it will get converted to radians

# Radians to Degrees conversion
radians = math.pi
print(math.degrees(radians)) # Use degrees function, input must be radians then it will get converted to degrees
