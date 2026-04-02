from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.food import Food
from app.models.food_entry import FoodEntry
from app.models.user import User
from app.schemas.entry import FoodEntryCreate, FoodEntryOut, DailyNutritionTotals

router = APIRouter(prefix="/entries", tags=["entries"])


@router.post("", response_model=FoodEntryOut, status_code=201)
def create_entry(
    payload: FoodEntryCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    food = db.query(Food).filter(Food.id == payload.food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    entry = FoodEntry(user_id=user.id, **payload.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.get("", response_model=list[FoodEntryOut])
def list_entries(
    consumed_date: date,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return (
        db.query(FoodEntry)
        .filter(FoodEntry.user_id == user.id, FoodEntry.consumed_date == consumed_date)
        .order_by(FoodEntry.consumed_at.desc())
        .all()
    )


@router.get("/daily-summary", response_model=DailyNutritionTotals)
def daily_summary(
    consumed_date: date,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    totals = (
        db.query(
            func.coalesce(func.sum(Food.calories * FoodEntry.servings), 0.0),
            func.coalesce(func.sum(Food.protein * FoodEntry.servings), 0.0),
            func.coalesce(func.sum(Food.carbs * FoodEntry.servings), 0.0),
            func.coalesce(func.sum(Food.fat * FoodEntry.servings), 0.0),
        )
        .join(Food, Food.id == FoodEntry.food_id)
        .filter(FoodEntry.user_id == user.id, FoodEntry.consumed_date == consumed_date)
        .first()
    )

    calories, protein, carbs, fat = totals
    return DailyNutritionTotals(
        date=consumed_date,
        calories=round(calories, 2),
        protein=round(protein, 2),
        carbs=round(carbs, 2),
        fat=round(fat, 2),
        calories_goal=user.daily_calorie_goal,
        protein_goal=user.daily_protein_goal,
        carbs_goal=user.daily_carb_goal,
        fat_goal=user.daily_fat_goal,
    )
