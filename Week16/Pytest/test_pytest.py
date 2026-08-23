import pytest

# For pytest module to work, the file name must start with test_*.py or *_test.py.
# Pytest then test those functions which are named starting with test_*
# We run it using the command pytest -v
# Output would look like test_pytest.py::test_inventory_loads_correctly PASSED

# FIXTURES

# 1. SCOPE & YIELD (Session Setup/Teardown)
@pytest.fixture(scope="session")
def store_inventory():
    """Starts once per session to load the massive store inventory."""
    print("\n[SETUP] Booting up inventory system...")
    inventory = {"apple": 5, "banana": 2}
    
    yield inventory  # Hands the inventory to whatever needs it
    
    print("\n[TEARDOWN] Shutting down inventory system...")
    inventory.clear()


# 2. COMPOSITION (Fixture depending on a fixture)
# Uses the default "function" scope, so it runs fresh per test.
@pytest.fixture
def empty_cart(store_inventory):
    """Creates a fresh shopping cart, but needs to check inventory first."""
    print("\n[PREP] Grabbing a new, empty shopping cart...")
    # The cart is just an empty dictionary
    cart = {} 
    
    # We are pretending the cart needs to know what store it belongs to
    cart["store_items_available"] = len(store_inventory)
    
    return cart


# TESTS (Discovery & Asserts)

# 3. TEST DISCOVERY & ASSERTS
def test_inventory_loads_correctly(store_inventory):
    # Pytest runs this because it starts with "test_"
    # It crashes (fails) if bananas don't equal 2
    assert store_inventory["banana"] == 2

def test_add_item_to_cart(empty_cart):
    # empty_cart was provided fresh by the fixture
    empty_cart["apple"] = 1
    
    # We assert it was added successfully
    assert "apple" in empty_cart
    assert empty_cart["apple"] == 1

def test_cart_is_actually_empty_at_start(empty_cart):
    # Because empty_cart is "function" scope, the apple from the 
    # previous test is gone. We have a fresh cart!
    assert "apple" not in empty_cart
