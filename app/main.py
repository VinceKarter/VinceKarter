from fastapi import FastAPI

from app.api import auth, foods, entries, users
from app.db.session import Base, engine
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(foods.router)
app.include_router(entries.router)
