from typing import Union
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    def __init__(self, username: str, is_active: bool = True) -> None:
        super().__init__()
        self.is_active = is_active
        self.username = username


class Expenditure(Base):
    __tablename__ = "expenditure"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String)
    user: User = relationship("User")

    def __init__(
        self, user: User, description: Union[None, str], category: str, amount: float
    ) -> None:
        super().__init__()
        self.user = user
        self.user_id = user.id
        self.description = description
        self.amount = amount
        self.category = category
