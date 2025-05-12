from datetime import datetime

from pydantic import (Field, EmailStr, field_validator,  model_validator, ValidationError, HttpUrl)
from pydantic import BaseModel
from datetime import datetime, timedelta

class Event(BaseModel):
    title:str
    date:datetime
    location:str

    @model_validator(mode='before')
    def future_time(cls, values):
        v_date = values.get('date')
        v_location = values.get('location')
        if (v_date < datetime.now() + timedelta(days=5)) and (v_location == 'Lima'):
            raise ValueError("Я туда так быстро не успею")
        if v_location == "Voronez":
            raise ValueError('Fuck you!')

try:
    future_event = Event(
        title="New Year Party",
        date=datetime.now() - timedelta(days=1),
        location="Lima")
    print(future_event)
except ValueError as e:
    print(e)