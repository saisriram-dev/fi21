import pytest

# Assert based tests
def test_math():
    result = 10 + 5
    # Pytest checks this. If it equals 15, the test passes. 
    # If it equals anything else, the test fails.
    assert result == 15


# Pytest WILL run this because it starts with "test_"
def test_subtraction():
    assert 10 - 2 == 8

# Pytest WILL NOT run this because it doesn't start with "test_"
def helper_function():
    return True

# A fixture is a prep-cook function. It prepares data or objects that your tests need. 
# You use the @pytest.fixture tag above the function to label it. 
# To use it, a test just asks for it by name in the parentheses.
@pytest.fixture
def default_user():
    # This prepares the data
    return {"name": "John", "age": 30}

def test_user_age(default_user):
    # The test receives the dictionary automatically
    assert default_user["age"] == 30


# There are three scopes for fixtures: function, module, and session.
# Function scope means the fixture is created for each test function that uses it.
# Module scope means the fixture is created once per module
# Session scope means the fixture is created once for the entire test session.
# This will only create the network connection ONCE, 
# even if 1,000 tests ask for it.
@pytest.fixture(scope="session")
def heavy_network_connection():
    return "Connected to server"


"""
If we were to write a function that should run after giving the output also like
when we are opening a file -> return contents of the file -> Then we need to close it too,
In such cases return is not enough, we need to use yield. Yield is a keyword that allows us to 
return a value and then continue executing the function after the test has run. 
This is useful for cleanup tasks. This is known as a teardown. The code after the yield statement 
will run after the test has completed.
"""
@pytest.fixture
def file_manager():
    # SETUP: Run before the test
    file = open("test_file.txt", "w")
    
    yield file # PAUSE: Hand the file to the test
    
    # TEARDOWN: Run after the test finishes
    file.close()

# Fixture composition
# Fixtures can ask for other fixtures. 
# This lets you build complex setups like LEGO bricks without writing messy, repetitive code.
@pytest.fixture
def raw_data():
    return [1, 2, 3]

# This fixture asks for the raw_data fixture above!
@pytest.fixture
def processed_data(raw_data):
    # It adds 10 to every number in the raw_data
    return [x + 10 for x in raw_data]


# Parametrization
def is_valid_password(pwd: str) -> bool:
    return len(pwd) >= 8 and any(c.isdigit() for c in pwd)

@pytest.mark.parametrize(
    "password, expected", 
    [
        ("Password123", True),   # Happy path
        ("short1", False),       # Too short
        ("NoDigitsHere", False), # No digits
        ("12345678", True),      # All digits, length >= 8
        ("", False),             # Empty string
    ]
)
def test_is_valid_password(password, expected):
    # Pytest will run this function 5 separate times
    assert is_valid_password(password) == expected

# Cross product / Stacking
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_cross(x, y):
    pass # Runs (0,2), (0,3), (1,2), (1,3)


# pytest.raises()
# Function we want to test
def divide(a, b):
    # If b is 0, Python raises ZeroDivisionError
    return a / b


# Our test
def test_divide_by_zero():

    # pytest.raises() means:
    # "I EXPECT this code to raise ZeroDivisionError"
    with pytest.raises(ZeroDivisionError):

        # This will raise ZeroDivisionError
        # because 10 cannot be divided by 0
        divide(10, 0)
        # Output would be: pytest_module.py::test_divide_by_zero PASSED
