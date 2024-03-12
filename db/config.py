from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

from db.models import Base


engine = create_engine(
    'postgresql+psycopg2://postgres:552216742@localhost:5432/postgres',
    pool_pre_ping=True
)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)
