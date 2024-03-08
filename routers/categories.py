
from fastapi import APIRouter, HTTPException, Query
from starlette import status
from database import models
from database.database import engine
from sqlmodel import Session, create_engine

router = APIRouter(prefix ='/categories', tags=['categories'])

@router.post("/create")
async def create_category(category: models.Category):
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category
