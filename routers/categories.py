"""
Module for handling category routes.
"""

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select
from starlette import status

from database import models
from database.database import engine

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=list[models.Category])
async def get_categories(offset: int = 0,
                         limit: int = Query(default=30, le=100)):
    """
    Get a list of categories.

    Args:
        offset (int): The offset value for pagination.
        limit (int): The limit value for pagination.

    Returns:
        list[models.Category]: The list of categories.
    """
    with Session(engine) as session:
        categories = session.exec(
            models.Category.__table__.select().offset(offset).limit(limit)
            ).all()
    return categories


@router.get("/{category_name:str}", response_model=models.Category)
async def get_category_by_name(category_name: str):
    """
    Get a category by its name.

    Args:
        category_name (str): The name of the category.

    Returns:
        models.Category: The category object.
    """
    with Session(engine) as session:
        category = session.exec(
            select(models.Category)
            .where(models.Category.name == category_name)
            ).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Category not found")
    return category


@router.post("/create", response_model=models.Category)
async def create_category(category: models.CategoryCreate):
    """
    Create a new category.

    Args:
        category (models.Category): The category object to be created.

    Raises:
        HTTPException: If the category name is missing or too long.

    Returns:
        models.Category: The created category object.
    """
    with Session(engine) as session:
        db_category = models.Category.model_validate(category)
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category
