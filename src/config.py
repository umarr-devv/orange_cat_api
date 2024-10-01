import pydantic


class DataBaseConfig(pydantic.BaseModel):
    database: str = 'orange_cat'
    host: str = 'localhost'
    user: str = 'postgres'
    password: str = 'qal3ko8tFgzyuL3vBeQW55UFNN9KcLJfeRisBhugm3NYc0WoUIKbzThf8sn0SWKY'
    echo: bool = False

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.database}"


class Config(pydantic.BaseModel):
    db: DataBaseConfig


config = Config(
    db=DataBaseConfig()
)
