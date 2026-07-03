from fastapi import FastAPI, UploadFile, Form

from resume_parser import extract_text
from profile_agent import create_profile

from ranking_agent import rank_opportunities
from planning_agent import create_plan
from collector import load_opportunities

from database import engine, SessionLocal, Base
from auth_models import User
from schemas import UserCreate, UserLogin
from auth import hash_password, verify_password

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Career Agent Backend Running"
    }


# -----------------------------
# Resume Upload Endpoint
# -----------------------------
@app.post("/upload")
async def upload_resume(
    file: UploadFile,
    age: int = Form(...),
    annual_income: int = Form(...),
    category: str = Form(...),
    state: str = Form(...),
    career_interest: str = Form(...)
):

    text = extract_text(file.file)

    student_data = {
        "age": age,
        "annual_income": annual_income,
        "category": category,
        "state": state,
        "career_interest": career_interest
    }

    profile = create_profile(
        text,
        student_data
    )

    return profile


# -----------------------------
# Register Endpoint
# -----------------------------
@app.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {
            "message": "Email already registered"
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User registered successfully"
    }


# -----------------------------
# Login Endpoint
# -----------------------------
@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return {
            "message": "User not found"
        }

    if not verify_password(
        user.password,
        existing_user.password
    ):
        return {
            "message": "Incorrect password"
        }

    return {
        "message": "Login successful",
        "name": existing_user.name,
        "email": existing_user.email
    }
