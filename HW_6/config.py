import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

class Config:
    DEBUG: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/database.db'

class DevelopmentConfig(Config):
    DEBUG: bool = True
    print(f"Database URI: {os.getenv('SQLALCHEMY_DATABASE_URI')}")

class ProductionConfig(Config):
    pass