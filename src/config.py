import pydantic


class DataBaseConfig(pydantic.BaseModel):
    database: str
    host: str
    user: str
    password: str
    echo: bool

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.database}"


class Config(pydantic.BaseModel):
    db: DataBaseConfig


config = Config(
    db=DataBaseConfig()
)
