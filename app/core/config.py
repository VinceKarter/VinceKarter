from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Food Tracker API"
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    database_url: str = "sqlite:///./food_tracker.db"


settings = Settings()
