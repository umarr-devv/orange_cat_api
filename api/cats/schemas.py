import pydantic


class CatSchema(pydantic.BaseModel):
    color: str | None = None
    age_in_month: int = 0
    description: str | None = None


class CatGetSchema(CatSchema):
    cat_id: int
    breed_id: int | None


class CatDetailSchema(CatSchema):
    breed_id: int
    breed_name: str | None
    breed_description: str | None


class CatCreateSchema(CatSchema):
    breed_id: int | None


class CatUpdateSchema(CatSchema):
    cat_id: int


class CatDeleteSchema(pydantic.BaseModel):
    cat_id: int
