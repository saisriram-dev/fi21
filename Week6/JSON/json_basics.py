# ----------> JSON <----------

# JSON = JavaScript Object Notation
# JSON is a syntax for storing and exchanging data.

""" 
Rules:
    1. All keys must be strings.
    2. They must be double quoted.
    3. Any string must be double quoted.
    4. There shouldn't be any trailing comma.
    
    Eg. 1. Python dict: {'name': 'A', 'age': 20, 'is_student': True, 'address': None}
           JSON: {"name": "A", "age": 20, "is_student": true, "address": null}
        
        2. data = {"name": "Bhavith", "age": 21}  (Python data structure)
           json_text = '{"name": "Bhavith", "age": 21}' (text representation of data)

    JSON module operations:
    JSON string → Python object
    Python object → JSON string
    JSON file → Python object
    Python object → JSON file
"""

import json

# Converting a JSON text into a Python object
json_text = '{"name": "Sri Ram", "age": 21, "skills": ["Python", "JSON"]}'
new_data = json.loads(json_text) # Converts the input json string to python dictionary
print(new_data)
print(type(new_data))
print(new_data["name"])

# Converting a Python object into a JSON string
python_dict = {'anime': 'Boku no Hero Academia', 
               'info': {'episodes': 170, 'seasons': 8, 'imdb': 8.3},
               'rating': 8.3}
data2 = json.dumps(python_dict) # Converts the input python dictionary to json string
print(data2)                    
print(type(data2))

# Converting JSON file into a Python object
with open("C:\\Users\\P SAI SRI RAM\\OneDrive\\Desktop\\fi21\\Week6\\JSON\\data.json", "r") as file:
    data3 = json.load(file)

print(data3)
print(type(data3))
print(data3["name"])

# Converting python object into a JSON file
data4 = {
    "anime": "Yakusoku no neverland",
    "seasons": 2,
    "imdb-score": 8.1
}

with open("C:\\Users\\P SAI SRI RAM\\OneDrive\\Desktop\\fi21\\Week6\\JSON\\output.json", "w") as file:
    json.dump(data4, file)

with open("Week6\JSON\output2.json", "w") as file:
    # To make the output more readable & arranged in a alphabetical order
    # We can use this while  using the "dumps" method too while converting python object into a JSON file
    json.dump(data4, file, indent=4, sort_keys=True)

data = {"word": "తెలుగు"}
print(json.dumps(data, ensure_ascii=False)) # This is to make sure that the non-ASCII characters are displayed

"""
    data = {"nums": {1, 2, 3}}
    json.dumps(data)

    The above code will throw an error because while dumps is used to convert a dictionary to 
    a JSON string, it cannot convert a set to a JSON string. Sets, tuples aren't JSON serializable.
    So we need to convert the set to a list. 
    
    The correct procedure is:
    data = {"nums": list({1, 2, 3})}
    json.dumps(data)
"""
