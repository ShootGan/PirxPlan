"""
This module is responsible for creating a SQLModel engine using
the database connection URL from the settings.
It uses the lru_cache decorator to cache the settings and avoid unnecessary file reads.
"""
from functools import lru_cache
from sqlmodel import create_engine
# from settings.settings import Settings

# @lru_cache()
# def get_settings():
#     return Settings()

# settings: Settings = get_settings()
database_connection_url = r'postgresql://postgres:<password>@localhost:5432/devdb'

engine = create_engine(database_connection_url, echo=True)
