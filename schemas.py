from typing import Union
from pydantic import BaseModel


class ExpenditureCreate(BaseModel):
    description: Union[str, None] = None
    amount: float
    category: str
    username: str


class UserCreate(BaseModel):
    username: str
