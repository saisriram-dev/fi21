from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserResponse(BaseModel):
    id: int
    username: str
    email: str


# response_model is used to filter out the password_hash field from the response
# What we supply to the response_model parameter is a Pydantic model that defines the shape of the
# response data. In this case, we are using the UserResponse model, which only includes the id, 
# username, and email fields. The password_hash field is not included in the UserResponse model, 
# so it will be filtered out from the response.
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "id": user_id,
        "username": "alice",
        "email": "alice@example.com",
        "password_hash": "SECRET"
    }
