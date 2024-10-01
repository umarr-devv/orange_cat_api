from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api.breeds.schemas import BreedCreateSchema, BreedGetSchema, BreedCatsSchema
from src.database import db
from src.repositories import BreedsRepository

router = APIRouter(prefix='/breeds')


@router.post('/create',
             response_model=BreedGetSchema)
async def create_breed(breed: BreedCreateSchema,
                       session: AsyncSession = Depends(db.session_dependency)):
    return await BreedsRepository.create(session, **breed.model_dump())


@router.get('/',
            response_model=list[BreedGetSchema])
async def get_all_breeds(session: AsyncSession = Depends(db.session_dependency)):
    return await BreedsRepository.get_all(session)


@router.get('/{breed_id}',
            response_model=list[BreedCatsSchema])
async def get_cats_by_breed_id(breed_id: int,
                               session: AsyncSession = Depends(db.session_dependency)):
    return await BreedsRepository.get_cats_by_breed_id(session, breed_id)
