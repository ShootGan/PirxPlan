from sqlmodel import SQLModel
import models
from database import engine

SQLModel.metadata.create_all(engine)