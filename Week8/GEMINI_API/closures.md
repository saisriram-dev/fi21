# Python Intermediate Concept: Closures

A **closure** is a function that remembers the variables from the scope in which it was created, even after that outer function has finished executing.

In simpler words, a closure allows an inner function to "carry" the data that existed when it was created.

---

## How Closures Work

When a function is defined inside another function, the inner function has access to:

- Its own local variables.
- Variables of the outer function.
- Global variables.

Normally, when the outer function finishes execution, its local variables disappear.

However, if the inner function is returned, Python keeps those variables alive because the inner function still needs them. This preserved environment is called a **closure**.

---

## Basic Example

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner


greet = outer()
greet()
```

Output

```text
Hello
```

Although `outer()` has already finished executing, `inner()` still remembers the value of `message`.

---

## Another Example

```python
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
```

Output

```text
10
15
```

Here,

```python
double
```

remembers

```python
x = 2
```

while

```python
triple
```

remembers

```python
x = 3
```

Each returned function has its own preserved variables.

---

## Visual Representation

```text
multiplier(2)

x = 2
│
└── multiply(y)
      │
      └── remembers x = 2
```

Even after `multiplier()` finishes, the value of `x` is stored inside the returned function.

---

## Inspecting a Closure

Python stores captured variables inside the `__closure__` attribute.

```python
def outer():
    x = 10

    def inner():
        return x

    return inner


func = outer()

print(func.__closure__)
```

Output

```text
(<cell at ...>,)
```

To view the stored value:

```python
print(func.__closure__[0].cell_contents)
```

Output

```text
10
```

---

## Closures with Multiple Variables

```python
def calculator(a, b):

    def add():
        return a + b

    return add


result = calculator(10, 20)

print(result())
```

Output

```text
30
```

The returned function remembers both `a` and `b`.

---

## Common Use Case: Function Factories

Closures are often used to create customized functions.

```python
def power(exponent):

    def raise_power(number):
        return number ** exponent

    return raise_power


square = power(2)
cube = power(3)

print(square(5))
print(cube(5))
```

Output

```text
25
125
```

Instead of repeatedly writing different functions, one function creates many specialized versions.

---

## Closures and Mutable Objects

A closure remembers the object, not a copy of it.

```python
def outer():
    numbers = []

    def add(num):
        numbers.append(num)
        return numbers

    return add


f = outer()

print(f(1))
print(f(2))
print(f(3))
```

Output

```text
[1]
[1, 2]
[1, 2, 3]
```

The same list is remembered between function calls.

---

## Modifying Captured Variables

Trying to modify an immutable variable directly causes an error.

```python
def outer():
    count = 0

    def inner():
        count += 1
        return count

    return inner
```

Output

```text
UnboundLocalError
```

Python thinks `count` is a new local variable.

To modify the captured variable, use `nonlocal`.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


counter = outer()

print(counter())
print(counter())
print(counter())
```

Output

```text
1
2
3
```

The `nonlocal` keyword tells Python to use the variable from the enclosing function instead of creating a new local variable.

---

## Closure vs Global Variable

Using globals:

```python
count = 0

def increment():
    global count
    count += 1
```

Using closures:

```python
def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Closures keep state private, while global variables can be modified from anywhere in the program.

---

## Advantages

- Keeps data private without using classes.
- Preserves state between function calls.
- Creates customized functions dynamically.
- Frequently used in decorators.
- Reduces reliance on global variables.

---

## Disadvantages

- Can be harder to understand for beginners.
- Captured objects remain in memory as long as the closure exists.
- Excessive nesting can reduce code readability.

---

## Summary

A closure is created when an inner function captures variables from its enclosing scope and continues to access them even after the outer function has finished executing. Python preserves these variables automatically, allowing functions to maintain state, create specialized behavior, and encapsulate data without requiring classes. Closures are widely used in function factories, decorators, callbacks, and stateful function designs.
