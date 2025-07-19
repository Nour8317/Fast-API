from sqlalchemy importfrom sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE = "postgresql://postgres:01149513302@localhost/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE)

SessionLocal = sessionmaker(autocommit=false, autoflush=false, bind=engine)
Base = declarative_base()