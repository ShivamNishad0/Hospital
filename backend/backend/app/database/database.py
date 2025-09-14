import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# For development, using SQLite
DATABASE_URL = "sqlite:///./clinicflow.db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(autoflush = False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
