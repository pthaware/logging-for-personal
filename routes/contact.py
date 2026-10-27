from fastapi import APIRouter

router = APIRouter()


@router.get("/contact")
def contact():
    return {"message": "Contact us at example@email.com"}
