from fastapi import FastAPI

"""
To run this file, use the following command:
First navigate to the directory where this file is located.

Then run:
uvicorn dynamic_urls:app --reload
"""

# The below line creates an instance of the FastAPI class
app = FastAPI()

"""
The {curly_braces} are used to define dynamic paths.
The value in the curly braces is a path parameter.
The path parameter is a variable that can be used in the function.

The path parameter is extracted from the URL and passed to the function.
They must use the same name as the path parameter.

So our function takes user_name as a parameter which is present in the URL (given by us only).
So if we give:
http://127.0.0.1:8000/hello/SriRam

The function will return:
{"User's Name": "SriRam"}
"""
@app.get("/hello/{user_name}")
def greet(user_name: str):
    return {"User's Name": user_name}
