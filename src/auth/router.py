from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.auth.models import role
from src.auth.schemas import RoleCreate


router = APIRouter(prefix='/roles', tags=['Roles'])


@router.get('')
async def get_all_roles(session: AsyncSession = Depends(get_async_session)):
    query = select(role)
    result = await session.execute(query)
    return {
        'status': 'success',
        'data': result.scalars().all(),
        'details': None,
    }


@router.post('')
async def create_role(new_role: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(role).values(**new_role.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 'success'}
