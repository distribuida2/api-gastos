from http import HTTPStatus
from pytest import fixture
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from models import Expenditure


class TestExpenditure:

    # client: TestClient

    # @classmethod
    # @fixture(scope="class", autouse=True)
    # def setup(self, client, db: Session):
    #     self.client = client

    # def test_post_expenditure_no_params(self):
    #     response = self.client.post("/expenditure/")
    #     assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    def test_post_expenditure_no_params(self, client):
        response = client.post("/expenditure/")
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
