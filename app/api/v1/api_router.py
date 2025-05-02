from fastapi import APIRouter
from .endpoints import auth, payments, webhooks

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
api_router.include_router(webhooks.router, prefix="/webhook", tags=["Webhooks"])