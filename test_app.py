from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_predict_female_first_class():
    response = client.post("/predict", json={
        "Pclass": 1, "Sex": 1, "Age": 25, "SibSp": 0,
        "Parch": 0, "Fare": 80, "Embarked": 1
    })
    assert response.status_code == 200
    assert response.json()["survived"] in [0, 1]


def test_predict_male_third_class():
    response = client.post("/predict", json={
        "Pclass": 3, "Sex": 0, "Age": 30, "SibSp": 0,
        "Parch": 0, "Fare": 8, "Embarked": 0
    })
    assert response.status_code == 200
    assert "result" in response.json()