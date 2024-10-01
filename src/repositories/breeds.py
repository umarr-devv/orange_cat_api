from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.baked import Result
from sqlalchemy.orm import joinedload

from src.models import Breed, Cat


class BreedsRepository:

    @staticmethod
    async def _create(session: AsyncSession,
                      name: str,
                      description: str | None = None) -> Breed:
        breed = Breed(name=name, description=description)
        session.add(breed)
        await session.commit()
        return breed

    @staticmethod
    async def create(session: AsyncSession,
                     name: str,
                     description: str | None = None) -> Breed:
        breed = await BreedsRepository.get_by_name(session, name)
        if breed:
            raise HTTPException(status_code=400,
                                detail='the name of the breed is not unique')
        return await BreedsRepository._create(session, name, description)

    @staticmethod
    async def get_by_name(session: AsyncSession,
                          name: str) -> Breed:
        statement = select(Breed).where(Breed.name == name)
        result: Result = await session.execute(statement)
        return result.scalar()

    @staticmethod
    async def get_by_id(session: AsyncSession,
                        breed_id: int) -> Breed:
        statement = select(Breed).where(Breed.breed_id == breed_id)
        result: Result = await session.execute(statement)
        return result.scalar()

    @staticmethod
    async def get_all(session: AsyncSession) -> list[Breed]:
        statement = select(Breed).order_by(Breed.breed_id)
        result: Result = await session.execute(statement)
        return result.scalars().all()

    @staticmethod
    async def _get_cats_by_breed_id(session: AsyncSession,
                                    breed_id: int) -> list[Cat]:
        statement = select(Breed).options(joinedload(Breed.cats)).where(Breed.breed_id == breed_id)
        result: Result = await session.execute(statement)
        breed: Breed = result.scalar()
        return breed.cats

    @staticmethod
    async def get_cats_by_breed_id(session: AsyncSession,
                                   breed_id: int) -> list[Cat]:
        breed = await BreedsRepository.get_by_id(session, breed_id)
        if not breed:
            raise HTTPException(
                status_code=400,
                detail='No such breed exists with this breed_id'
            )
        return await BreedsRepository._get_cats_by_breed_id(session, breed_id)
