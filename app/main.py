from fastapi import FastAPI
from app.api.v1.api_router import api_router
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Tunzaa Payment API", version="1.0.0")

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")