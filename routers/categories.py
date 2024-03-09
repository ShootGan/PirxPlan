
from fastapi import APIRouter, HTTPException, Query
from starlette import status
from database import models
from database.database import engine
from sqlmodel import Session, create_engine

router = APIRouter(prefix ='/categories', tags=['categories'])

@router.post("/create")
async def create_category(category: models.Category):
    if not category.name or not category.name.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category name is required")
    if len(category.name) > 30:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category name too long")
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category
