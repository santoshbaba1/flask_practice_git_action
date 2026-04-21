import pytest
from app import app, mongo
from bson.objectid import ObjectId


@pytest.fixture
def client():
    # Enable testing mode
    app.config["TESTING"] = True

    client = app.test_client()

    # ✅ Setup: clean DB and insert test data
    with app.app_context():
        mongo.db.students.delete_many({})

        mongo.db.students.insert_one({
            "_id": ObjectId("66fddff25f4b5f6a0a123456"),
            "name": "Test Student",
            "email": "test@student.com",
            "location": "Kanpur",
            "course": "Flask"
        })

    yield client

    # ✅ Teardown: clean DB after test
    with app.app_context():
        mongo.db.students.delete_many({})


# ✅ TEST HOME PAGE
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test Student" in response.data


# ✅ TEST ADD STUDENT
def test_add_student(client):
    data = {
        "name": "New User",
        "email": "new@user.com",
        "location": "Kanpur",
        "course": "Python"
    }

    response = client.post('/add', data=data, follow_redirects=True)

    assert response.status_code == 200
    assert b"New User" in response.data


# ✅ TEST UPDATE STUDENT
def test_update_student(client):
    student_id = "66fddff25f4b5f6a0a123456"

    data = {
        "name": "Updated Name",
        "email": "updated@student.com",
        "location": "Kanpur",
        "course": "Updated Course"
    }

    response = client.post(f'/update/{student_id}', data=data, follow_redirects=True)

    assert response.status_code == 200
    assert b"Updated Name" in response.data


# ✅ TEST DELETE STUDENT
def test_delete_student(client):
    # Insert temp student
    with app.app_context():
        student_id = mongo.db.students.insert_one({
            "name": "Temp User",
            "email": "temp@user.com",
            "location": "Kanpur",
            "course": "Temp Course"
        }).inserted_id

    response = client.get(f'/delete/{student_id}', follow_redirects=True)

    assert response.status_code == 200
    assert b"Temp User" not in response.data
