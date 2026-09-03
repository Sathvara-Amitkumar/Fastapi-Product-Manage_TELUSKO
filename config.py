from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql+psycopg2://postgres:123@localhost:5432/project_fastapi"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)