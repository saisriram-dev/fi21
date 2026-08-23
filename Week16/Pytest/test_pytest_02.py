import pytest
import asyncio

# --- The Application Code ---
async def fetch_user_profile(user_id: int) -> str:
    """Simulates fetching a user from a slow database."""
    await asyncio.sleep(0.1) # Simulate network delay
    
    database = {1: "Alice", 2: "Bob"}
    
    if user_id not in database:
        raise KeyError(f"User {user_id} not found")
        
    return database[user_id]


# --- The Combined Test ---
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_id, expected_name, expect_error",
    [
        (1, "Alice", False),   # Case 1: Valid user
        (2, "Bob", False),     # Case 2: Valid user
        (99, None, True),      # Case 3: Invalid user, EXPECT AN ERROR
    ]
)
async def test_fetch_user_profile(user_id, expected_name, expect_error):
    
    if expect_error:
        # We tell Pytest: "Watch this code, it MUST throw a KeyError."
        with pytest.raises(KeyError):
            # The execution pauses here for 0.1 seconds (the network delay).
            # If we had background tasks, they would run now.
            await fetch_user_profile(user_id)
            
    else:
        # Standard success path
        name = await fetch_user_profile(user_id)
        assert name == expected_name
