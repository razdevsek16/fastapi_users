from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_USER: str
    DATABASE_NAME: str
    DATABASE_HOSTNAME: str
    HOST: str
    

    class Config:
        env_file = './.env'


settings = Settings() # type: ignore