from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import repository
import models
import schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/expenditure/")
async def create_expenditure(
    expenditure: schemas.ExpenditureCreate, db: Session = Depends(get_db)
):
    user = repository.get_user_by_username(db, username=expenditure.username)
    return repository.create_expenditure(db, expenditure, user)


@app.post("/user/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = repository.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    return repository.create_user(db=db, user=user)
