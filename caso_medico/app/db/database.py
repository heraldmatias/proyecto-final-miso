from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import get_settings

settings = get_settings()
engine = create_engine(
    'postgresql://postgres:heqpe5-rocsih-ceXguw@proyecto-final-rds.cz4gwt9zq8cl.us-east-1.rds.amazonaws.com:5432/test_database',
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
