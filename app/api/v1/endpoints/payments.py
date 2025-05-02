from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.payment import create_payment_plan, add_savings, get_payment_plan
from app.schemas.payment import PaymentPlanCreate, PaymentPlan, SavingsCreate
from app.core.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/plans", response_model=PaymentPlan)
def create_plan(
    plan: PaymentPlanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_payment_plan(db, plan, current_user.id)


@router.post("/plans/{plan_id}/savings")
def save_money():
    return {"message": "Money saved successful"}