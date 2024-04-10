from pytest import fixture
from sqlalchemy.orm import Session
from fastapi import status
from typing import Union
from models import Expenditure, User
from schemas import ExpenditureCreate


class TestExpenditure:

    username: str = "test"
    user_id: Union[None, int] = -1

    @fixture(scope="function", autouse=True)
    def setup(self, db: Session):
        default_user = User(username=self.username)
        db.add(default_user)
        db.commit()
        db.refresh(default_user)
        self.user_id = default_user.id

    def test_post_expenditure_not_real_user(self, client, db):
        amount_before = len(db.query(Expenditure).all())
        expenditure = ExpenditureCreate(
            description="Gasto test",
            amount=12.4,
            category="categoria test",
            username="not real test",
        )
        response = client.post("/expenditure/", json=expenditure.model_dump())

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        amount_after = len(db.query(Expenditure).all())
        assert amount_after == amount_before

    def test_post_expenditure_no_params(self, client):
        response = client.post("/expenditure/")
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_post_expenditure_ok(self, client, db):
        amount_before = len(db.query(Expenditure).all())
        expenditure = ExpenditureCreate(
            description="Gasto test",
            amount=12,
            category="categoria test",
            username=self.username,
        )
        response = client.post("/expenditure/", json=expenditure.model_dump())
        assert response.status_code == status.HTTP_201_CREATED

        amount_after = len(db.query(Expenditure).all())
        assert amount_after == amount_before + 1

        data = response.json()
        assert data["user_id"] == self.user_id
        assert data["amount"] == expenditure.amount
        assert data["category"] == expenditure.category
        assert data["description"] == expenditure.description
