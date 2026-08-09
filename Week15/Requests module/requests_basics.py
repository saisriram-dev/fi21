import requests
import json

params = {
    "prompt": "A beautiful landscape with mountains and a river",
    "size": "1024x1024"
}

url = "https://image.example.com/data"

# Timeout is set to (3, 10) seconds, where 3 seconds is the connection timeout and 10 seconds is the read timeout
# 3 seconds is the maximum time to wait for a connection to be established
# 10 seconds is the maximum time to wait for a response after the connection is established
res = requests.get(url, params=params, timeout=(3, 10))
print(res.url)  # Print the constructed URL (which includes params) of the request for debugging purposes

# If we have an image output for a particular prompt, save it to a file
# Use wb mode to write binary data, as images are binary files
# And res.content contains the binary content of the response
if res.status_code == 200:
    with open("file.pdf", "wb") as f:
        f.write(res.content)

# To tell the server we are sending a JSON, we need to set the Content-Type header to application/json
url2 = "https://json_example.com/data"
response = requests.post(url2, data=json.dumps(params), headers={"Content-Type": "application/json"})

# To avoid the heavy lifting of Content-Type header, we can use the json parameter in requests.post() which automatically 
# sets the Content-Type to application/json
response = requests.post(url2, json=params)
