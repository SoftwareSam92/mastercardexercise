import asyncio
from cmath import e
import pytest
pytest_plugins = ('pytest_asyncio',)

from mock import patch
from unittest import mock 
from main import Account, get_account, add_account, delete_account, accounts

# The following tests are to test the functionality of the get_account method in main.

"""
Tests getting accounts when there is no data loaded into the application.
"""
@pytest.mark.asyncio
async def test_get_account_no_account():
    test = await get_account(1)
    assert test == None

"""
Tests the get account with the correct data and key in it.
"""
@pytest.mark.asyncio
@mock.patch('main.accounts', dict({0: Account(name="test",description="",balance=10,active=False)}))
async def test_get_account_one_account():
    test = await get_account(0)
    assert test == Account(name="test",description="",balance=10,active=False)

"""
tests accounts with a different id then has been specified.
"""
@pytest.mark.asyncio
@mock.patch('main.accounts', dict({1: Account(name="test",description="",balance=10,active=False)}))
async def test_get_account_one_account_wrong_id():
    test = await get_account(0)
    assert test == None


# Tests for add_account()

@pytest.mark.asyncio
@mock.patch('main.accounts', dict())
async def test_add_account_add_one():
    test = await add_account(0, Account(name="test",description="",balance=10,active=False))
    assert test == Account(name="test",description="",balance=10,active=False)
    output = await get_account(0)
    assert output == {'active': False, 'balance': 10.0, 'description': '', 'name': 'test'}

@pytest.mark.asyncio
@mock.patch('main.accounts', dict())
async def test_add_account_none_valid():
    test = None
    try:
        test = await add_account(0, {"test": 1})
    except:
        test = True
        assert True
    assert test != None

@pytest.mark.asyncio
@mock.patch('main.accounts', dict({1: Account(name="test",description="",balance=10,active=False)}))
async def test_add_account_add_dup():
    test = await add_account(1, Account(name="test",description="",balance=10,active=False))
    assert test == None

# Delete tests

@pytest.mark.asyncio
@mock.patch('main.accounts', dict( {2: Account(name='test', description='', balance=10.0, active=False) } ) )
async def test_delete_account_valid():
    assert await delete_account(2)
    assert accounts == {}
