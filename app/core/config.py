from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator

class Settings(BaseSettings):
    # Application Settings
    APP_NAME: str = "FastAPI MongoDB"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 1
    RELOAD: bool = True

    # MongoDB Settings
    MONGODB_URL: str
    DATABASE_NAME: str
    MONGODB_MAX_CONNECTIONS: int = 100
    MONGODB_MIN_CONNECTIONS: int = 1

    # Security Settings
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    # CORS Settings
    CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    CORS_CREDENTIALS: bool = True
    CORS_METHODS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]

    # Logging Settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "console"
    LOG_FILE: str = "logs/app.log"
    LOG_ROTATION: str = "500 MB"
    LOG_RETENTION: str = "10 days"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 