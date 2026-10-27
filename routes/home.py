from fastapi import APIRouter

router = APIRouter()


@router.get("/home")
def home():
    return {"message": "Welcome to the Home page"}
