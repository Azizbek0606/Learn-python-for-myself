from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from lesson_15_config import get_db
from lesson_15_schemas import StudentSchema

app = FastAPI()


@app.get("/students")
async def example(db: Session = Depends(get_db)):
    stmt = db.execute(text("select * from students"))
    mapping_res = stmt.mappings().all()
    return mapping_res


@app.post("/students")
async def create_student(students: StudentSchema, db: Session = Depends(get_db)):
    try:
        insert_run = """INSERT INTO students (name, age) VALUES (:name, :age)"""
        db.execute(text(insert_run), students.model_dump())
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(status_code = 500 , detail=str(e))
    finally:
        db.commit()
        db.close()