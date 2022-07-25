import asyncio
import pytest
pytest_plugins = ('pytest_asyncio',)

from main import get_account

@pytest.mark.asyncio
async def test_get_account():
    test = await get_account(1)
    assert test == None