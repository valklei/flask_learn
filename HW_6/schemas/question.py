from pydantic import BaseModel, Field, ConfigDict

class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=5)
    category_id: int | None = None

class CategoryInQuestion(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int
    category: CategoryInQuestion
    model_config = ConfigDict(from_attributes=True)

