from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.products.router import product_router
from app.users.router import user_router
app = FastAPI()

app.include_router(product_router, prefix="/product")
app.include_router(user_router)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
