from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

sqlalchemy_database_uri = os.environ.get(
    "SQLALCHEMY_DATABASE_URI", "postgresql://postgres:postgres@127.0.0.1:5432/aiohttp-app"
)

@dataclass
class Config:
    SQLALCHEMY_DATABASE_URI: str = sqlalchemy_database_uri
    HOST: str = os.environ.get("HOST", "127.0.0.1")
    PORT: int = os.environ.get("PORT", 8000)
