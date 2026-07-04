from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Settings:
    baserow_url: str = os.getenv("BASEROW_URL", "")
    baserow_token: str = os.getenv("BASEROW_TOKEN", "")
    database_id: str = os.getenv("DATABASE_ID", "")


settings = Settings()