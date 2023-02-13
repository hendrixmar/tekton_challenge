from fastapi import status, HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.users.deps import get_current_user, create_login_session

from app.users.schemas import UserOut, UserAuth, TokenSchema, SystemUser

from app.utils import get_hashed_password
from uuid import uuid4
from app.users.deps import db

user_router = APIRouter()


@user_router.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # querying database to check if user already exist
    user = db.get(data.email)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    db[data.email] = user  # saving user to database
    return user


@user_router.post('/login',
                  summary="Create access and refresh tokens for user",
                  response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return create_login_session(form_data)

