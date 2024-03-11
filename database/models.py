from datetime import datetime, timedelta
from typing import List, Optional

from pydantic import field_validator, model_validator
from sqlmodel import Field, Relationship, SQLModel


class CategoryBase(SQLModel):
    name: str = Field(index=True, max_length=30, unique=True)

    @field_validator("name")
    @classmethod
    def name_validate(cls, v: str) -> str:
        if v.isnumeric():
            raise ValueError("Name must not be a number")
        if not v.strip():
            raise ValueError("Name must not be empty")
        return v


class Category(CategoryBase, table=True):
    __tablename__ = "categories"
    id: Optional[int] = Field(default=None, primary_key=True)
    objects: List["Object"] = Relationship(back_populates="category")


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Object(SQLModel, table=True):
    __tablename__ = "objects"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    category_id: int = Field(foreign_key="categories.id")
    category: Category = Relationship(back_populates="objects")
    reservations: List["Reservation"] = Relationship(back_populates="object")


class ReservationBase(SQLModel):
    start_time: datetime
    end_time: datetime
    object_id: int = Field(foreign_key="objects.id")

    @model_validator(mode="after")
    def check_start_time_is_before_end_time(self) -> "ReservationBase":
        start_time = self.start_time
        end_time = self.end_time
        if start_time >= end_time:
            raise ValueError("start_time must be before end_time")
        return self

    @field_validator("start_time")
    @classmethod
    def check_start_time_is_not_in_past(cls, v: datetime) -> datetime:
        if v < (datetime.now() - timedelta(minutes=1)):
            raise ValueError("start_time must not be in the past")
        return v


class Reservation(ReservationBase, table=True):
    __tablename__ = "reservations"
    id: Optional[int] = Field(default=None, primary_key=True)
    object: Object = Relationship(back_populates="reservations")


class ReservationCreate(ReservationBase):
    object_name: Optional[str] = None
