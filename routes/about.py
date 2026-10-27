from fastapi import APIRouter
import logging

router = APIRouter()


@router.get("/about")
def about():
    for i in range(10):
        logging.info(i)
    return {"message": "This is the About page"}