from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.session import Base


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    brand = Column(String, nullable=True)
    serving_size = Column(Float, nullable=False)
    serving_unit = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    protein = Column(Float, default=0)
    carbs = Column(Float, default=0)
    fat = Column(Float, default=0)

    entries = relationship("FoodEntry", back_populates="food")
