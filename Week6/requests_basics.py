# Requests enable our python code to make HTTP requests to a server

# A get request is used when you want to retrieve data from a server

"""
    Status Codes:
    200 → success
    201 → created
    400 → bad request
    401 → unauthorized
    403 → forbidden
    404 → not found
    500 → server error
"""

import requests

# Sends a request to the url and stores the response object given by the url inside the response variable
url = "https://api.github.com"
response = requests.get(url)

# To print the status code
print(response.status_code)
if response.status_code == 200:
    print("Success")
else:
    print("Error")

# Better version to implement the code from the lines 18 to 27
url = "https://api.github.com"
response = requests.get(url)
response.raise_for_status() # Raises an error if status code is something other than 2xx
print("Request worked")

# Usually API gives JSON data. To convert it into a Python object like a dictioanry or a list
# we use .json()
data = response.json() # If the response is not valid JSON, response.json() can raise JSONDecodeError
print(type(data))
print(data)

# Better version to implement the code from the lines 35 to 39
response = requests.get(url)
try:
    data = response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Response was not valid JSON")

# HEADERS
# Headers are used to send additional information with the request
headers = {
    "User-Agent": "MyPythonApp/1.0", # This is a custom header
    "Accept": "application/json" # This tells the server that we want to receive JSON data in the response
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.headers)
print(response.headers.get("Content-Type"))
