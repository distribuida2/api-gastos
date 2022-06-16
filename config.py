from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    sqlalchemy_database_test: str = "sqlite://"
    app_name: str

    class Config:
        env_file = ".env"


settings = Settings()
