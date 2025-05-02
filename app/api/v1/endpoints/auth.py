from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    return {"message": "User created successful"}


@router.post("/login")
def login():
    return {"message": "User logged-in successful"}