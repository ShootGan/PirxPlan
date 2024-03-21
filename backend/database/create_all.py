from sqlmodel import SQLModel
import models  # noqa: F401
from database import engine

SQLModel.metadata.create_all(engine)
