from pydantic import BaseModel, Field, ConfigDict

class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=10)
    category_id: int = Field(..., gt=0)


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int | None = None
    model_config = ConfigDict(
        from_attributes=True
    )