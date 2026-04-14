# Student Registration System

A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **Environment Variables:** Managed via `.env` file

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mohanDevOps-arch/flask_Practice.git
cd flask_Practice
```

<img width="1365" height="763" alt="code push" src="https://github.com/user-attachments/assets/a3d9d181-16bb-4b57-a60d-d751ddc6aa44" />


### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
Flask
Flask-PyMongo
python-dotenv
bson
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
MONGO_URI=mongodb+srv://santosharma:2TNVQGuJsJvRy0pT@travelmemorydb.0kzvz9q.mongodb.net/studentDB

```

### 5. Run the application

```bash
python app.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## Project Structure
<img width="1363" height="760" alt="app1" src="https://github.com/user-attachments/assets/1379aaa2-f4a0-4d72-812e-03021f9390ab" />

```
project/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
│
├── app.py
├── requirements.txt
└── .env
```

---

## Screenshots

**Home Page**
Lists all students with Edit/Delete buttons.

- <img width="1363" height="760" alt="app1" src="https://github.com/user-attachments/assets/44424662-e054-4a44-8eb3-28faf510caf6" />


**Add Student**
Form to add a new student.
- <img width="1897" height="801" alt="image" src="https://github.com/user-attachments/assets/d65d25c3-ebb5-410a-adb1-e130ad7c5878" />

- <img width="1363" height="760" alt="app1" src="https://github.com/user-attachments/assets/87966331-2606-4958-aa1a-4183ddf32ab9" />

**Update Student**
Form pre-filled with student details.
- <img width="1361" height="752" alt="app reg" src="https://github.com/user-attachments/assets/e3c3979d-b23c-4d5e-a7ca-859854d7655c" />

- <img width="1365" height="767" alt="app update" src="https://github.com/user-attachments/assets/88d74b1a-071e-4e83-9fe5-a5b3a1da09c5" />

---

## Notes

* Make sure MongoDB is running and accessible via the URI in `.env`
* Delete action includes a confirmation page to prevent accidental deletion
* Uses `ObjectId` from `bson` to work with MongoDB document IDs

- <img width="1365" height="767" alt="mongodb" src="https://github.com/user-attachments/assets/3527b924-0db9-4c50-a51d-212d06255e57" />
- <img width="1365" height="761" alt="docker build 1" src="https://github.com/user-attachments/assets/269c3a60-cc91-406a-b24b-87cf99951399" />
- <img width="1365" height="767" alt="docker build" src="https://github.com/user-attachments/assets/90c4fee9-7ed4-4da7-99ae-dd13aa29b2e7" />

---

## License

MIT License


Author

Santosh Kumar Sharma (12394), Batch-15

DevOps & Cloud Enthusiast
---



