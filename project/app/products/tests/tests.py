import pytest
from httpx import AsyncClient
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_hero(
        async_client: AsyncClient,
        async_session: AsyncSession
):
    response = await async_client.get("/ping")

    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
