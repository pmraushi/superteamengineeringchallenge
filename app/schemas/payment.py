from pydantic import BaseModel

class PaymentPlanCreate(BaseModel):
    name: str
    total_amount: float

class PaymentPlan(BaseModel):
    id: int
    user_id: int
    total_amount: float
    saved_amount: float
    class Config:
        from_attributes = True

class SavingsCreate(BaseModel):
    amount: float

class PaymentCompletedEvent(BaseModel):
    plan_id: int
    amount: float