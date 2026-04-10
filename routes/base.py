from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1",
)

@router.get("/welcome")
def welcome():
    return {"message": "Welcome to FastAPI!"}