from datetime import date, datetime
from pydantic import BaseModel


class FoodEntryCreate(BaseModel):
    food_id: int
    meal_type: str
    servings: float = 1.0
    consumed_date: date


class FoodEntryOut(BaseModel):
    id: int
    food_id: int
    meal_type: str
    servings: float
    consumed_date: date
    consumed_at: datetime

    class Config:
        from_attributes = True


class DailyNutritionTotals(BaseModel):
    date: date
    calories: float
    protein: float
    carbs: float
    fat: float
    calories_goal: float
    protein_goal: float
    carbs_goal: float
    fat_goal: float
