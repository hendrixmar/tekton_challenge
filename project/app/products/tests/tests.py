import pytest
from httpx import AsyncClient
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.products.models import Product

@pytest.mark.asyncio
async def test_create_hero(async_client: AsyncClient, async_session: AsyncSession):
    response = await async_client.get("/ping")

    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


@pytest.mark.asyncio
async def test_bruh(async_client: AsyncClient, async_session: AsyncSession):
    response = await async_client.get("/product")

    assert response.status_code == 200
    result = await async_session.execute(select(Product))
    temp = result.scalars().all()
    print(temp)
    assert response.json() == temp
