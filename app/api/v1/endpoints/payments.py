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
def save_money(
    plan_id: int,
    savings: SavingsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    plan = get_payment_plan(db, plan_id)
    if not plan or plan.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Plan not found or unauthorized")
    total_saved = add_savings(db, plan_id, savings.amount)
    if total_saved >= plan.total_amount:
        # Simulate merchant payout to console/terminal (log for now)
        print(f"Payout triggered for plan {plan_id}: TZS {plan.total_amount} to merchant")
        # In a real system, trigger webhook here
    return {"total_saved": total_saved, "target_reached": total_saved >= plan.total_amount}