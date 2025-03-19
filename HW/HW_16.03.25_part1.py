from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    city: str
    street: str
    house_number: int
class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    address: Address

# Представление JSON строки
json_string = """{ "name": "John Doe", "age": 22, "email": "john.doe@example.com", "address": { "city": "New York", "street": "5th Avenue", "house_number": 123 } }"""