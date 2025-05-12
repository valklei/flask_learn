from pydantic import (Field, EmailStr, field_validator,  model_validator, ValidationError, HttpUrl)
from pydantic import BaseModel

class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)
    url: HttpUrl


class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0,lt=120)
    email: EmailStr
    is_employed: bool
    address:Address

    @field_validator('name')
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only letters')
        return value

    @field_validator('email')
    def check_email_domain(cls, value: str) -> str: # value="test.email@gmail.com"  # value="test.email@gmail.com"
        allowed_domains = {"com", 'net', 'org'}
        raw_domain = value.split('.')[-1]
        if raw_domain not in allowed_domains:
            raise ValueError(f"Email must be from one of the following domains: {', '.join(allowed_domains)}")
    def check_age(cls, values):
        age = values.get('age')
        is_employed = values.get('is_employed')
        if is_employed and (age < 18 or age > 65):
            raise ValueError('Employed users must be between 18 and 65 years old')
        return values

try:
    user_valid = User(name="Vlad", age=22, email="test.email@gmail.com", is_employed=False, address=Address(city="New York", street="5th Avenue", house_number=123, url="https://www.google.com"))
    print(user_valid)
    user_invalid=User(name="Marin2", age=18, email="test.email@gmail.com", is_employed=False, address=Address(city="New York", street="5th Avenue", house_number=123, url="https://www.google.com"))

except ValidationError as e:
    print(f'Ошибка валидации край: {e.json()}')


