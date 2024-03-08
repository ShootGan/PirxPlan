from fastapi import FastAPI
from routers import reservations, categories

DESCRIPTION = """App for managing reservations"""
VERSION = "0.1.0"
tags_metadata = [
    {
        "name": "reservation",
        "description": "Operations with reservations."
    },
    {
        "name": "category",
        "description": "Operations with categories."
    }
]
app = FastAPI(title = "Reservation API", description = DESCRIPTION,
              version = VERSION,
              openapi_tags = tags_metadata)
app.include_router(reservations.router)
app.include_router(categories.router)