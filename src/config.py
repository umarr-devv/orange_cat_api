import pydantic


class DataBaseConfig(pydantic.BaseModel):
    database: str = 'postgres'
    host: str = 'db'
    user: str = 'postgres'
    password: str = 'secret_password'
    echo: bool = False

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.database}"


class Config(pydantic.BaseModel):
    db: DataBaseConfig


config = Config(
    db=DataBaseConfig()
)
