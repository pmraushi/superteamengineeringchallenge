from fastapi import APIRouter, HTTPException
from app.schemas.payment import PaymentCompletedEvent

router = APIRouter()

@router.post("/payment-completed")
def payment_completed(event: PaymentCompletedEvent):
    # Log webhook event (in production, verify signature and process)
    print(f"Payment completed for plan {event.plan_id}: TZS {event.amount}")
    return {"status": "received"}