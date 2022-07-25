import asyncio
from typing import Dict, Optional, Union

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel


class Account(BaseModel):
    name: str
    description: Optional[str] = None
    balance: float
    active: bool = True


app = FastAPI()

accounts = dict()


async def get_account(account_id: int) -> Optional[Account]:
    if account_id in accounts:
        return accounts[account_id]
    else:
        return None


async def add_account(account_id: int, account: Account) -> Optional[Account]:
    if account_id in accounts:
        return None
    else:
        accounts[account_id] = account.dict()
        return accounts[account_id]


async def delete_account(account_id: int) -> Optional[bool]:
    if account_id in accounts:
        return True
    else:
        return None


@app.get("/healthz")
async def get_health(request: Request) -> Union[Optional[Dict], HTTPException]:
    return {"status": True}


@app.get("/accounts/{account_id}")
async def read_account(account_id: int):
    res = await get_account(account_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Account not found")
    else:
        return res


@app.put("/accounts/{account_id}", status_code=201)
async def create_account(account_id: int, account: Account):
    res = await add_account(account_id, account)
    if res is None:
        raise HTTPException(status_code=409, detail="Account exists")
    else:
        return res


@app.delete("/accounts/{account_id}", status_code=200)
async def remove_account(deleted: Optional[bool]):
    if deleted is None:
        raise HTTPException(status_code=404, detail="Account not found")
    else:
        return {"msg": "Successful"}
