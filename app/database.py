from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./SqLiteDB.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL,
                       connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# connection to Database
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()