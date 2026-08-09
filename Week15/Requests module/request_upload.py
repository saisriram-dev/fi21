# Uploading files using requests library in Python
import requests

url = 'https://example.com/upload' 

# Path to the file I want to upload
file_path = 'path/to/my/file.txt'  

with open(file_path, 'rb') as f:
    res = requests.post(url, files={'file': f})
