from sqlalchemy import Column, Integer, Float, ForeignKey, Date, DateTime, func, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class FoodEntry(Base):
    __tablename__ = "food_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False, index=True)
    consumed_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    consumed_date = Column(Date, nullable=False, index=True)
    meal_type = Column(String, nullable=False, default="snack")
    servings = Column(Float, nullable=False, default=1.0)

    user = relationship("User", back_populates="entries")
    food = relationship("Food", back_populates="entries")
