from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from baumapp.schemas import OperationCreate
from baumapp.database import get_async_session
from baumapp.models.models import book

router = APIRouter(
    prefix='/books',
    tags=['Books']
)

@router.get('/')
async def get_books(avg_x: float, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(book).where(book.c.x_avg_count_in_line <= avg_x)
        result = await session.execute(query)
        return {
            'status': 'success',
            'data': result.mappings().all(),
            'details': None,
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': None,
        })

@router.post('/')
async def add_books(operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(book).values(**operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
