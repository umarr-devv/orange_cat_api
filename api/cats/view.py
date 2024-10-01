from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.cats.schemas import CatCreateSchema, \
    CatUpdateSchema, CatGetSchema, CatDeleteSchema, CatDetailSchema
from src.database import db
from src.repositories import CatsRepository

router = APIRouter(prefix='/cats', tags=['cats'])


@router.post('/create',
             response_model=CatCreateSchema,
             status_code=status.HTTP_201_CREATED)
async def post_cat(cat: CatCreateSchema,
                   session: AsyncSession = Depends(db.session_dependency)):
    return await CatsRepository.create(session, **cat.model_dump())


@router.patch('/edit',
              response_model=CatGetSchema,
              status_code=status.HTTP_200_OK)
async def edit_cat(cat: CatUpdateSchema,
                   session: AsyncSession = Depends(db.session_dependency)):
    return await CatsRepository.edit(session, **cat.model_dump())


@router.delete('/delete',
               status_code=status.HTTP_200_OK)
async def delete_cat(cat: CatDeleteSchema,
                     session: AsyncSession = Depends(db.session_dependency)):
    await CatsRepository.delete(session, cat_id=cat.cat_id)
    return {
        'detail': 'success'
    }


@router.get('/{cat_id}')
async def get_cat(cat_id: int,
                  session: AsyncSession = Depends(db.session_dependency)):
    cat = await CatsRepository.get(session, cat_id)
    return CatDetailSchema(
        color=cat.color,
        age_in_month=cat.age_in_month,
        description=cat.description,
        breed_id=cat.breed.breed_id,
        breed_name=cat.breed.name,
        breed_description=cat.breed.description
    )


@router.get('/',
            response_model=list[CatGetSchema])
async def get_all_cats(session: AsyncSession = Depends(db.session_dependency)):
    return await CatsRepository.all(session)
