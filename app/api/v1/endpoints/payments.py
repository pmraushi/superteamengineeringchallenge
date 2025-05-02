from fastapi import APIRouter

router = APIRouter()

@router.post("/plans")
def create_plan():
    return {"message": "Plan created successful"}


@router.post("/plans/{plan_id}/savings")
def save_money():
    return {"message": "Money saved successful"}