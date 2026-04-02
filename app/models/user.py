from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    daily_calorie_goal = Column(Float, default=2000)
    daily_protein_goal = Column(Float, default=120)
    daily_carb_goal = Column(Float, default=250)
    daily_fat_goal = Column(Float, default=70)

    entries = relationship("FoodEntry", back_populates="user", cascade="all, delete-orphan")
