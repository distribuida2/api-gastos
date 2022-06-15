from sqlalchemy.orm import Session
import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    filtered_users = db.query(models.User).filter(models.User.username == username)
    return filtered_users.first()


def create_expenditure(
    db: Session, expenditure: schemas.ExpenditureCreate, user: models.User
):
    db_expenditure = models.Expenditure(
        user=user,
        description=expenditure.description,
        category=expenditure.category,
        amount=expenditure.amount,
    )
    db.add(db_expenditure)
    db.commit()
    db.refresh(db_expenditure)
    return db_expenditure


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
