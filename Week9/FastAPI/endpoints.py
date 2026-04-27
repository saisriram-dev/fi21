from fastapi import FastAPI

"""
To run this file, use the following command:
First navigate to the directory where this file is located.

Then run:
uvicorn endpoints:app --reload
"""

# The below line creates an instance of the FastAPI class
app = FastAPI()

"""
The below line is a decorator that outputs the function whenever we access the endpoint '/'
The function path will be like: http://127.0.0.1:8000/

For eg, if endpoint is:
@app.get("/hello")
def hi():
    return {"message": "Hello World"}

So the hi() runs if url="http://127.0.0.1:8000/hello"
""" 
@app.get("/")
def first_message():
    return {"message": "I love pizza!!!"}

"""
Workflow:
Browser -> Request -> Uvicorn -> FastAPI -> Response -> Browser
"""
