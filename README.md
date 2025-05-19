# FastAPI + PostgreSQL - 

This is a simple FastAPI-based RESTful API for managing student data. 
It uses SQLAlchemy for ORM, PostgreSQL for the database, and Pydantic for data validation.


## Requirements

- Python 3.9+
- PostgreSQL installed and running
- `pip` (Python package manager)


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/theeSagar/FastAPI.git
cd your-repo

### Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate

### To run the server
uvicorn main:app --reload
