import pytest
import httpx
from auth_service import process_user_login

@pytest.mark.asyncio
async def test_process_user_login_success(mocker):
    # 1. Patch the async network call
    # mocker automatically makes this an AsyncMock because the target is `async def`
    mock_fetch = mocker.patch("auth_service.fetch_external_profile")
    mock_fetch.return_value = {"is_active": True, "name": "Alice"}
    
    # 2. Patch the async database call
    mock_db = mocker.patch("auth_service.log_login_event")
    
    # 3. Execute the function under test
    result = await process_user_login("user_123")
    
    # 4. Assert the logic worked
    assert result is True
    
    # 5. Verify the mocks were AWAITED (not just called)
    mock_fetch.assert_awaited_once_with("user_123")
    mock_db.assert_awaited_once_with("user_123")

@pytest.mark.asyncio
async def test_process_user_login_inactive_user(mocker):
    mock_fetch = mocker.patch("auth_service.fetch_external_profile")
    # Return an inactive profile
    mock_fetch.return_value = {"is_active": False, "name": "Bob"}
    
    mock_db = mocker.patch("auth_service.log_login_event")
    
    result = await process_user_login("user_456")
    
    assert result is False
    # The database should NEVER have been awaited because the user is inactive
    mock_db.assert_not_awaited()

@pytest.mark.asyncio
async def test_process_user_login_api_failure(mocker):
    mock_fetch = mocker.patch("auth_service.fetch_external_profile")
    # Simulate an HTTP error being raised during the network call
    mock_fetch.side_effect = httpx.HTTPError("API Down")
    
    result = await process_user_login("user_789")
    
    # The try/except block in our code should catch the error and return False
    assert result is False