from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = "password123"
    database_name: str = "my_db_name"
    database_username: str = "postgres"
    secret_key: str = "MY_SECRET_KEY"
    algorithm: str = "HS_#_#_#"
    access_token_exp_time: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
