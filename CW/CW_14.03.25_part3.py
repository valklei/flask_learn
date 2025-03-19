from pydantic import BaseModel, Field, AliasChoices


class Event(BaseModel):
    title: str

    class Config:
       validate_assignment = True
       str_strip_whitespace = True
       str_min_length = 5


event = Event(title="     Summary 1       ")

print(event)
event.title = 'Hi'
print(event)