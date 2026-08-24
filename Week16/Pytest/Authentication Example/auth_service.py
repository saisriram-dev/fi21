import httpx
import asyncio
from database import db_pool # Assume that there is a database file

async def fetch_external_profile(user_id: str) -> dict:
    """Makes a real HTTP request to an external identity provider."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.identity.com/users/{user_id}")
        response.raise_for_status()
        return response.json()

async def log_login_event(user_id: str) -> None:
    """Writes to our local database asynchronously."""
    query = "INSERT INTO logins (user_id) VALUES ($1)"
    await db_pool.execute(query, user_id)

async def process_user_login(user_id: str) -> bool:
    """The main business logic we want to test."""
    try:
        # 1. Fetch user data
        profile = await fetch_external_profile(user_id)
        
        # 2. Check business logic
        if not profile.get("is_active"):
            return False
            
        # 3. Log the event
        await log_login_event(user_id)
        return True
        
    except httpx.HTTPError:
        return False
