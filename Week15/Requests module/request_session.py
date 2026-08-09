# Sessions in Requests module in Python
# Sessions improve the performance of our application by reusing the underlying TCP connection for multiple requests to the same host. 
# Used to persist certain parameters across requests
# The default ones such as cookies, headers, etc. can be set in a session object and will be used for all requests made with that session.
import requests

session = requests.Session()
url = "https://api.example.com/data"

# Now whenever we make a request using this session object, these headers will be sent along with the request.
session.headers.update(
    {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json",
    }
)

# Streaming a large file using a session
# Streaming is useful when downloading large files, as it allows us to download the file in chunks rather than loading the 
# entire file into memory at once into the RAM. This is especially important for large files, as it can help prevent memory issues and 
# improve performance.

# The below code is for streaming media like video or audio files, or large datasets. 
# It reads the response in chunks and writes them to a file on disk.
with session.get(url, stream=True, timeout=(5, 10)) as response:
    response.raise_for_status()  # Raise an exception for HTTP errors

    with open("file.bin", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192): # Read in 8KB chunks
            if chunk:  
                f.write(chunk)

# If we were to stream text content, we could use the iter_lines() method instead of iter_content().
with session.get(url, stream=True, timeout=(5, 10)) as response:
    response.raise_for_status()  # Raise an exception for HTTP errors

    with open("file.txt", "w") as f:
        for line in response.iter_lines():
            if line:  
                f.write(line.decode('utf-8') + '\n')

    """
    Or, if we want to process the lines as they arrive from the server, we can do something like this:
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
    
        # Process each line as it arrives from the server
        for line in response.iter_lines():
            if line:
                # line is bytes; decode to string if needed
                print("Received line:", line.decode("utf-8"))
    """
