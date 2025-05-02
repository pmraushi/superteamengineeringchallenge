from fastapi import APIRouter

router = APIRouter()

@router.post("/payment-completed")
def payment_completed():
    return {"message": "Payment completed"}