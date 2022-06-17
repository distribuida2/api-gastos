from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, status
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


@app.post(
    "/expenditure/",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "content": {"application/json": {}},
            "description": "Username no existente",
        }
    },
    status_code=status.HTTP_201_CREATED,
    tags=["gastos"],
)
async def create_expenditure(
    expenditure: schemas.ExpenditureCreate, db: Session = Depends(get_db)
):
    user = repository.get_user_by_username(db, username=expenditure.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username no existente"
        )
    return repository.create_expenditure(db, expenditure, user)


@app.post(
    "/user/",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "content": {"application/json": {}},
            "description": "Username ya registrado",
        }
    },
    tags=["usuarios"],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = repository.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username ya registrado"
        )
    return repository.create_user(db=db, user=user)
