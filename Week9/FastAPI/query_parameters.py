from fastapi import FastAPI

app = FastAPI()

"""
If we were to use an attribute in the function,
then it will be considered as a query parameter.

It means that when we go the url, we can pass the attribute as a query parameter.
Eg: http://127.0.0.1:8000/?name=John (Query Parameters follow '?')

    If we don't include query parameter:
    http://127.0.0.1:8000/
    we will get an error as the function needs a name query parameter to run.
"""


@app.get("/")
def greet(name: str):
    return {"message": f"Hello {name}!"}


# If we didn't provide a query parameter, it will take "User" as the default value
@app.get("/home/")
def home(name: str = "User"):
    return {"message": f"Welcome to the home page, {name}!"}
