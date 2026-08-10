import asyncio

from typing import Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field, EmailStr


app = FastAPI()


# This model defines what we expect when a user sends us a request
class UserRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=100
    )

    email: EmailStr

    # Phone is optional, so we set a default of None
    phone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=15
    )


# This is what we'll send back to the client when they hit the dashboard endpoint
class DashboardResponse(BaseModel):
    user_id: int
    name: str
    orders: list
    notifications: list
    recommendations: list


# This function mimics checking a JWT token and getting the current user
# FastAPI will call this automatically before running our endpoint
async def get_current_user():
    # In a real app, we'd validate the token here
    await asyncio.sleep(0.1)

    return {
        "id": 100,
        "role": "user"
    }


# Fetches all orders for a user from the database
async def get_orders(user_id: int):
    # Simulating database call delay
    await asyncio.sleep(2)

    return [
        {"order_id": 101, "amount": 500},
        {"order_id": 102, "amount": 800},
    ]


# Gets notifications for the user from another service
async def get_notifications(user_id: int):
    # Simulating calling an external notification service
    await asyncio.sleep(2)

    return [
        {"message": "Your order has shipped"},
        {"message": "New discount available"},
    ]


# Grabs personalized product recommendations
async def get_recommendations(user_id: int):
    # Simulating a call to the recommendation engine
    await asyncio.sleep(2)

    return [
        {"product": "Laptop"},
        {"product": "Keyboard"},
    ]


# Main endpoint that builds the user dashboard
# Depends() tells FastAPI to run get_current_user first
@app.post(
    "/users/{user_id}/dashboard",
    response_model=DashboardResponse
)
async def get_dashboard(
    user_id: int,
    user: UserRequest,
    current_user=Depends(get_current_user)
):
    # Print the logged-in user info for debugging
    print("Logged-in user:", current_user)

    # Instead of waiting for orders, then notifications, then recommendations one by one,
    # we run all three at the same time with gather() to speed things up
    orders, notifications, recommendations = await asyncio.gather(

        get_orders(user_id),

        get_notifications(user_id),

        get_recommendations(user_id)
    )

    # Build and return the dashboard response with all the data we just fetched
    return {
        "user_id": user_id,
        "name": user.name,
        "orders": orders,
        "notifications": notifications,
        "recommendations": recommendations
    }
