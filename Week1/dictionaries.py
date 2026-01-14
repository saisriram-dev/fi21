# Dictionaries
# They usually contain key value pairs. They are in the form {key: value}
# They are ordered and changeable. No duplicates allowed.

# An example dictionary containg capitals as values and countries as keys
capitals = {"India": "Delhi",
            "Russia": "Moscow",
            "USA": "Washington D.C.",
            "China": "Beijing"}

# Accessing the dictionary
print(capitals.get("India"))
print(capitals.get("North Korea")) # Output is None

# Updating a dictionary
capitals.update({"Japan": "Tokyo"}) # This adds a country Japan along with it's capital as value
capitals.update({"China":"Need not know"}) # This updates the capital of the key China
                                           # Key value pair of China already exists in the dictionary
print(capitals)

# Pop method
capitals.pop("China") # This removes the key-value pair with key = "China"
print(capitals)

# Popitem method
anime_country = capitals.popitem() # It removes the most recent entry or simply the last pair
print(anime_country)
print(capitals)

# Using if-else with dictionaies
if capitals.get("Japan"): # If there is a key "Japan" then implement the if condition
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

# To get all the keys in a dictionary without including the values
keys = capitals.keys()
print(keys)

for key in keys: # Same as for key in capital.keys():
    print(key)

# To get all the values in a dictionary without including the keys
values = capitals.values()
print(values)

for value in values: # Sames as for value in capitals.values():
    print(value)

# Items method
items = capitals.items() # Creates a 2D list of tuples which contain the key-value pairs
print(items)

for key, value in items: # Same as for key, value in capitals.items():
    print(f"{value} is the capital of {key}.")

# Clear method
capitals.clear()
