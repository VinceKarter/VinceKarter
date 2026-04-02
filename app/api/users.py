from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserGoalUpdate, UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user


@router.put("/me/goals", response_model=UserOut)
def update_goals(
    payload: UserGoalUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    for key, value in payload.model_dump().items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
