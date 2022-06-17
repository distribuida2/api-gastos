from fastapi import status
from pytest import fixture
from sqlalchemy.orm import Session
from models import User

USERNAME = "test"


class TestUser:
    @fixture(scope="function", autouse=True)
    def setup(self, db: Session):
        db.add(User(username=USERNAME))

    def test_post_users_no_params(self, client):
        response = client.post("/user/")
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_post_users_ok(self, client, db: Session):
        amount_before = len(db.query(User).all())
        new_user_username = "test2"

        response = client.post("/user/", json={"username": new_user_username})

        amount_after = len(db.query(User).all())
        assert response.status_code == status.HTTP_201_CREATED
        assert amount_after == amount_before + 1

        data = response.json()
        assert data["username"] == new_user_username
        assert data["is_active"] == True

    def test_post_users_already_exists(self, client, db: Session):
        users = db.query(User).all()
        amount_before = len(db.query(User).all())

        response = client.post("/user/", json={"username": USERNAME})

        users = db.query(User).all()
        amount_after = len(users)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert amount_after == amount_before
