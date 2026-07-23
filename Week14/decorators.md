## Python Decorators

A **decorator** is a function that modifies or extends the behavior of another function without directly changing its original code. Decorators are widely used for logging, authentication, caching, timing, and access control.

In Python, functions are **first-class objects**, meaning they can be passed to and returned from other functions.

### Example

```python
def log_execution(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")
    return wrapper

@log_execution
def process_data():
    print("Processing data...")

process_data()
```

**Output:**

```text
Function started
Processing data...
Function finished
```

The statement:

```python
@log_execution
```

is essentially equivalent to:

```python
process_data = log_execution(process_data)
```

The decorator receives the original function, wraps it with additional behavior, and returns the new function.

### Decorators with Arguments

A more flexible decorator can handle functions with different parameters using `*args` and `**kwargs`:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))
```

Decorators are important because they support **separation of concerns**. Common functionality can be added to many functions without duplicating code. In production Python, decorators appear frequently in web frameworks, testing tools, caching systems, and authorization mechanisms.
