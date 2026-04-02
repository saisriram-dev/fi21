# Use of *args
def smart_sum(*args):
    total = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            total += arg
        elif type(arg) == list or type(arg) == tuple:
            total += sum(arg)
        else:
            continue
    return total


print(smart_sum(1, 2, [3, 4], (5, 6)))


# Use of **kwargs
def filter_kwargs(**kwargs):
    res = {}
    for key, value in kwargs.items():
        if type(value) == str and value.strip() != "":
            res[key] = value
    return res


print(filter_kwargs(name="Ram", age=21, city="", country="India"))


# This function calls another function
def call_func(func, args_list, kwargs_dict):
    return func(*args_list, **kwargs_dict)


print(call_func(smart_sum, [1, 2, [3, 4], (5, 6)], {}))


# UEnforcing keyword only arguments with *
def create_account(username, *, password):
    return f"Account created for {username} with password {'*' * len(password)}"


print(create_account("ram", password="1234"))


# Using both *args and **kwargs
def greet(*args, **kwargs):
    title = kwargs.get("title", "")
    uppercase = kwargs.get("uppercase", False)
    for arg in args:
        if uppercase:
            title = title.upper()
            print(f"HELLO {title} {arg.upper()}")
        else:
            print(f"Hello {title} {arg}")
    return


print(greet("Ram", "Shyam", "Hari", title="Mr.", uppercase=True))
