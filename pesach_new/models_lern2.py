from datetime import datetime
from pydantic import (BaseModel, Field, EmailStr, field_validator, model_validator,
                      ValidationError)

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime
    class Config:
        json_encoders = { datetime: lambda v: v.strftime('%d-%m-%Y %H:%M') }
        str_strip_whitespace = True
        str_min_length = 2
        validate_assignment = True
user = User(first_name='Valerii  ', last_name='Kl', email='val@icloud.com', created_at=datetime.now())
print(user)
print(user.model_dump_json())  # Выводит время регистрации пользователя в заданном формате

user.first_name ='Alex   ' #, last_name='Kl', email='val@icloud.com', created_at=datetime.now())
print(user)
print(user.model_dump_json())