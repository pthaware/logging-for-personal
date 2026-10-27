from fastapi import APIRouter

from routes.home import router as home_router
from routes.about import router as about_router
from routes.contact import router as contact_router

router = APIRouter()

router.include_router(home_router)
router.include_router(about_router)
router.include_router(contact_router)