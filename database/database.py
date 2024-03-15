"""
This module is responsible for creating a SQLModel engine using
"""

# from functools import lru_cache

from sqlmodel import create_engine

# from settings.settings import Settings

# @lru_cache()
# def get_settings():
#     return Settings()

# settings: Settings = get_settings()
database_connection_url = r"postgresql://postgres:superSecretPassword@postgress:5432/devdb"  # noqa: E501

engine = create_engine(database_connection_url, echo=True)
