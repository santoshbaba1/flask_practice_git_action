import os
import pytest
from app import app, mongo
from bson.objectid import ObjectId


@pytest.fixture
def client():
    """Create test client with isolated test DB"""

    app.config["TESTING"] = True

    # ✅ Use environment variable (SECURE)
    app.config["MONGO_URI"] = os.getenv(
        "MONGO_URI",
        "mongodb://192.168.1.8:27017/test_students_db"
    )

    client = app.test_client()

    with app.app_context():
        # Clean database before tests
        mongo.db.students.delete_many({})

        # Insert test data
        mongo.db.students.insert_one(
            {
                "_id": ObjectId("66fddff25f4b5f6a0a123456"),
                "name": "Test Student",
                "email": "test@student.com",
                "location": "Kanpur",
                "course": "DevOps",
            }
        )

    yield client

    with app.app_context():
        # Cleanup after tests
        mongo.db.students.delete_many({})
    
def test_home_page(client):
    """Test home page loads correctly"""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Test Student" in response.data


def test_add_student(client):
    """Test adding student"""
    data = {
        "name": "New User",
        "email": "new@user.com",
        "location": "Kanpur",
        "course": "DevOps",
    }

    response = client.post("/add", data=data, follow_redirects=True)

    assert response.status_code == 200
    assert b"New User" in response.data


def test_update_student(client):
    """Test updating student"""
    student_id = "66fddff25f4b5f6a0a123456"

    data = {
        "name": "Updated Name",
        "email": "updated@student.com",
        "location": "Kanpur",
        "course": "Updated Course",
    }

    response = client.post(
        f"/update/{student_id}",
        data=data,
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Updated Name" in response.data


def test_delete_student(client):
    """Test deleting student"""

    with app.app_context():
        student_id = mongo.db.students.insert_one(
            {
                "name": "Temp User",
                "email": "temp@user.com",
                "location": "Kanpur",
                "course": "Temp Course",
            }
        ).inserted_id

    response = client.get(f"/delete/{student_id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"Temp User" not in response.data
