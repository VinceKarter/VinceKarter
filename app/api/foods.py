from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.food import Food
from app.models.user import User
from app.schemas.food import FoodCreate, FoodOut

router = APIRouter(prefix="/foods", tags=["foods"])


@router.post("", response_model=FoodOut, status_code=201)
def create_food(payload: FoodCreate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    food = Food(**payload.model_dump())
    db.add(food)
    db.commit()
    db.refresh(food)
    return food


@router.get("", response_model=list[FoodOut])
def list_foods(
    q: str | None = Query(default=None, description="Search by name or brand"),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    query = db.query(Food)
    if q:
        like = f"%{q.lower()}%"
        query = query.filter((Food.name.ilike(like)) | (Food.brand.ilike(like)))
    return query.order_by(Food.name.asc()).all()


@router.get("/{food_id}", response_model=FoodOut)
def get_food(food_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    food = db.query(Food).filter(Food.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food
