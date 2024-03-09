from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=30)
    objects: List["Object"] = Relationship(back_populates="category")

class Object(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    category_id: int = Field(foreign_key="category.id")
    category: Category = Relationship(back_populates="objects")
    reservations: List["Reservation"] = Relationship(back_populates="object")

class Reservation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_time: datetime
    end_time: datetime
    object_id: int = Field(foreign_key="object.id")
    object: Object = Relationship(back_populates="reservations")