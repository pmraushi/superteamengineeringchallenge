from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class PaymentPlan(Base):
    __tablename__ = "payment_plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = Column(Float, nullable=False)
    saved_amount = Column(Float, default=0.0)
    user = relationship("User")

class Savings(Base):
    __tablename__ = "savings"
    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("payment_plans.id"), nullable=False)
    amount = Column(Float, nullable=False)
    plan = relationship("PaymentPlan")