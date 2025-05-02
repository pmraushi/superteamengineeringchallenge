from sqlalchemy.orm import Session
from app.models.payment import PaymentPlan, Savings
from app.schemas.payment import PaymentPlanCreate

def create_payment_plan(db: Session, plan: PaymentPlanCreate, user_id: int):
    db_plan = PaymentPlan(user_id=user_id, total_amount=plan.total_amount, saved_amount=0.0)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def get_payment_plan(db: Session, plan_id: int):
    return db.query(PaymentPlan).filter(PaymentPlan.id == plan_id).first()

def add_savings(db: Session, plan_id: int, amount: float):
    plan = get_payment_plan(db, plan_id)
    if not plan:
        return None
    db_saving = Savings(plan_id=plan_id, amount=amount)
    db.add(db_saving)
    plan.saved_amount += amount
    db.commit()
    return plan.saved_amount