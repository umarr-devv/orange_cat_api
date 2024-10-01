import pydantic


class BreedSchema(pydantic.BaseModel):
    description: str | None


class BreedCreateSchema(BreedSchema):
    name: str


class BreedGetSchema(BreedCreateSchema):
    breed_id: int


class BreedCatsSchema(pydantic.BaseModel):
    cat_id: int
    color: str | None = None
    age_in_month: int = 0
    description: str | None = None
