from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.cats.schemas import CatCreateSchema, \
    CatUpdateSchema, CatGetSchema, CatDeleteSchema, CatDetailSchema
from src.database import db
from src.repositories import CatsRepository

router = APIRouter(prefix='/cats')


@router.post('/create',
             response_model=CatCreateSchema,
             status_code=status.HTTP_201_CREATED)
async def post_cat(cat: CatCreateSchema,
                   session: AsyncSession = Depends(db.session_dependency)):
    return await CatsRepository.create(session, **cat.model_dump())
