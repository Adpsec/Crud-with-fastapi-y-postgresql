from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "postgresql://postgres:postgres@localhost:5435/fast_db"
engine = create_engine(SQLALCHEMY_DB_URL)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
        db.close()