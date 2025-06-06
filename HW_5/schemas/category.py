from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    id: int
    name: str = Field(..., min_length=5)


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=10)