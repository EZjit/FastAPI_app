from sqlalchemy import insert, select

from src.tests.conftest import client, async_session_maker
from src.auth.models import role


async def test_add_role():
    async with async_session_maker() as session:
        statement = insert(role).values(name='admin', permissions=None)
        await session.execute(statement)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], 'Role is note added'


def test_register():
    response = client.post('/auth/register', json={
        "email": "user@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    })
    assert response.status_code == 201, 'user doesnt created'

