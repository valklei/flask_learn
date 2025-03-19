from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool


user = User(
    id=1,
    name="Dima",
    age=23,
    is_active=True
)

print(user)

print(user.name)


my_var: int

#print(my_var)
