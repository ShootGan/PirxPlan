from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """
    Represents the settings for the application.

    Attributes:
        database_connection_url (str): The URL for the database connection.
    """
    database_connection_url: str 
