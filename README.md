# FastAPI MongoDB Project

This is a FastAPI project with MongoDB integration.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=your_database_name
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000
API documentation will be available at http://localhost:8000/docs 