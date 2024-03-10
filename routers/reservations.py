from fastapi import APIRouter, HTTPException, Query
from starlette import status
from database import models
from database.database import engine
from sqlmodel import Session, select
from typing import Optional
from datetime import timedelta, datetime

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/", response_model=list[models.Reservation])
async def get_reservation(offset: int = 0, limit: int = Query(default=30, le=100)):
    with Session(engine) as session:
        reservations = session.exec(
            select(models.Reservation).offset(offset).limit(limit)
        ).all()
    return reservations


@router.post("/create", response_model=models.Reservation)
async def create_reseravation(reseravation: models.ReservationCreate):

    if not reseravation.object_id and not reseravation.object_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either object_id or object_name must be provided",
        )
    with Session(engine) as session:
        if not reseravation.object_id:
            object_to_reserve = session.exec(
                select(models.Object).where(
                    models.Object.name == reseravation.object_name
                )
            ).first()
            if not object_to_reserve:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Object not found"
                )
            reseravation.object_id = object_to_reserve.id

        reservation_overlap = session.exec(
            select(models.Reservation)
            .where(models.Reservation.object_id == reseravation.object_id)
            .where(models.Reservation.start_time < reseravation.end_time)
            .where(models.Reservation.end_time > reseravation.start_time)
        ).all()
        if reservation_overlap:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Reservation overlaps with existing reservation",
            )

        db_reservation = models.Reservation.model_validate(reseravation)
        session.add(db_reservation)
        session.commit()
        session.refresh(db_reservation)
    return db_reservation
