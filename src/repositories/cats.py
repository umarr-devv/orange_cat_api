from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.baked import Result
from sqlalchemy.orm import joinedload

from src.models import Cat
from src.repositories.breeds import BreedsRepository


class CatsRepository:

    @staticmethod
    async def _create(session: AsyncSession,
                      breed_id: int,
                      color: str | None = None,
                      age_in_month: int | None = None,
                      description: str | None = None) -> Cat:
        cat = Cat(color=color, age_in_month=age_in_month,
                  description=description, breed_id=breed_id)
        session.add(cat)
        await session.commit()
        return cat

    @staticmethod
    async def create(session: AsyncSession,
                     breed_id: int,
                     color: str | None = None,
                     age_in_month: int | None = None,
                     description: str | None = None) -> Cat:
        breed = await BreedsRepository.get_by_id(session, breed_id)
        if not breed:
            raise HTTPException(status_code=400,
                                detail='Theres no such thing as a breed of cat with that breed_id')
        return await CatsRepository._create(session, breed_id, color, age_in_month, description)

    @staticmethod
    async def _get(session: AsyncSession, cat_id: int) -> Cat:
        statement = select(Cat).options(joinedload(Cat.breed)).where(Cat.cat_id == cat_id)
        result: Result = await session.execute(statement)
        return result.scalar()

    @staticmethod
    async def get(session: AsyncSession, cat_id: int) -> Cat:
        cat = await CatsRepository._get(session, cat_id)
        if not cat:
            raise HTTPException(status_code=400,
                                detail='cat with that cat_id does not exist')
        return cat

    @staticmethod
    async def all(session: AsyncSession) -> list[Cat]:
        statement = select(Cat).order_by(Cat.cat_id)
        result: Result = await session.execute(statement)
        return result.scalars().all()

    @staticmethod
    async def edit(session: AsyncSession,
                   cat_id: int,
                   color: str | None = None,
                   age_in_month: int | None = None,
                   description: str | None = None) -> Cat:
        cat = await CatsRepository.get(session, cat_id)
        cat.color = color if color else cat.color
        cat.age_in_month = age_in_month if age_in_month else cat.age_in_month
        cat.description = description if description else cat.description
        await session.commit()
        return cat

    @staticmethod
    async def delete(session: AsyncSession, cat_id: int):
        cat = await CatsRepository.get(session, cat_id)
        await session.delete(cat)
        await session.commit()
