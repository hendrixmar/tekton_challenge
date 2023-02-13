from pydantic.types import PositiveInt

from pydantic import condecimal, EmailStr
from sqlmodel import Field, SQLModel
from decimal import Decimal


class UserAuth(SQLModel, table=True):
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")

