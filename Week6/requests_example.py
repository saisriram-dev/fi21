import requests

url = "https://api.github.com"

headers = {
    "Accept": "application/json",  # This tells the server that we want to receive JSON data in the response
}

response = requests.get(
    url, headers=headers, timeout=10
)  # This will set a timeout of 10 seconds
response.raise_for_status()  # This will raise an exception if the response status code is not 2xx

print("Status code: ", response.status_code)

data = (
    response.json()
)  # Tghis will convert the response content into a Python dictionary
print(data)
