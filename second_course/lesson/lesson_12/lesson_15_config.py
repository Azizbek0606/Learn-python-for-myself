from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:Azizbek.5474@localhost:5432/university")

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()