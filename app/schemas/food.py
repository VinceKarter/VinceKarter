from pydantic import BaseModel


class FoodBase(BaseModel):
    name: str
    brand: str | None = None
    serving_size: float
    serving_unit: str
    calories: float
    protein: float = 0
    carbs: float = 0
    fat: float = 0


class FoodCreate(FoodBase):
    pass


class FoodOut(FoodBase):
    id: int

    class Config:
        from_attributes = True
