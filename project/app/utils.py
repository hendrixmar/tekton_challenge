import abc

from sqlmodel import SQLModel
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = r"\wug2Df1}y2\c?o_I$?'o-~*vOs3XR/=g:~BRM#I;IN4<1nUF0v%Ey37kz^rER"
# os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = (
    "E51C6DD89D2E40309C2D6CBC42DAE63DF029A96A30DDDD310D682A1E30A75A90"
)


# os.environ['JWT_REFRESH_SECRET_KEY']


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference: int) -> dict:
        raise NotImplementedError

    @abc.abstractmethod  # (1)
    def modify(self, batch: dict) -> dict:
        raise NotImplementedError  # (2)

    @abc.abstractmethod
    def delete(self, reference: int) -> dict:
        raise NotImplementedError
