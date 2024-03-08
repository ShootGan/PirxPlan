
from fastapi import APIRouter, HTTPException, Query
from starlette import status

router = APIRouter(prefix ='/reservations', tags=['reservations'])

@router.get("/")
async def get_reservation():
    return {"message": "Get all reservations"}