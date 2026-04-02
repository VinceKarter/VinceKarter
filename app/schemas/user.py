from pydantic import BaseModel, EmailStr


class UserGoalUpdate(BaseModel):
    daily_calorie_goal: float
    daily_protein_goal: float
    daily_carb_goal: float
    daily_fat_goal: float


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    daily_calorie_goal: float
    daily_protein_goal: float
    daily_carb_goal: float
    daily_fat_goal: float

    class Config:
        from_attributes = True
