from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    city: str
    street: str
    house_number: int

class User(BaseModel):
    name:str
    age:int
    email: EmailStr
    address:Address

user_data = """
{
    "name": "exec 'ls /'",
    "age": "2_128",
    "email": "john.doee@xample.a",
    "address": {
        "city": "New York",
        "street": "St. Time Square",
        "house_number": 2
    }
}
"""

user = User.model_validate_json(user_data)

print(user)

user = User(
    first_name='Vlad',
    last_name="Black",
    age=23
)

print(user)

admin = Admin(
    first_name='Jessika',
    last_name="Black",
    age=27,
    salary_rating=2.4,
)
print(admin)

moder = Moderator(
    first_name='Mila',
    last_name="Green",
    age=31,
    phone='+1234567890',
)
print(moder)


from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(
        min_length=4,
        max_length=15,
        description="Name of user"
    )
    last_name: str = Field(
        default="Black",
        min_length=2,
        max_length=30,
    )
    age: int = Field(
        gt=0,
        lt=100
    )


user = User(
    first_name='John',
    age=19
)

print(user)

from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError


class User(BaseModel):
    name: str = Field(
        min_length=4,
        max_length=15
    )
    age: int = Field(
        gt=0,
        lt=100
    )
    email: EmailStr

    @field_validator('email')
    @classmethod
    def check_email_domain(cls, value: str) -> str: # value="test.email@gmail.com"
        allowed_domains = {"gmail.com",}
        raw_domain = value.split('@')[-1]

        if raw_domain not in allowed_domains:
            raise ValueError(f"Email must be from one of the following domains: {', '.join(allowed_domains)}")

        return value

Petru Vatov 12:16
+