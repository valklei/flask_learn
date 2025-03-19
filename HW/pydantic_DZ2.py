# Разработать систему регистрации пользователя, используя
# Pydantic для валидации входных данных, обработки вложенных структур
# и сериализации. Система должна обрабатывать данные в формате JSON.
#
# Задачи:
# Создать классы моделей данных с помощью Pydantic для пользователя и
# его адреса.
# Реализовать функцию, которая принимает JSON строку, десериализует
# её в объекты Pydantic, валидирует данные, и в случае успеха сериализует
# объект обратно в JSON и возвращает его.
# Добавить кастомный валидатор для проверки соответствия возраста и
# статуса занятости пользователя.
# Написать несколько примеров JSON строк для проверки различных сценариев валидации: успешные регистрации и случаи, когда валидация не проходит (например возраст не соответствует статусу занятости).
# Модели:
# Address: Должен содержать следующие поля:
# city: строка, минимум 2 символа.
# street: строка, минимум 3 символа.
# house_number: число, должно быть положительным.
# User: Должен содержать следующие поля:
# name: строка, должна быть только из букв, минимум 2 символа.
# age: число, должно быть между 0 и 120.
# email: строка, должна соответствовать формату email.
# is_employed: булево значение, статус занятости пользователя.
# address: вложенная модель адреса.
# Валидация:
# Проверка, что если пользователь указывает, что он
# занят (is_employed = true), его возраст должен быть от 18 до 65 лет.


from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, ValidationError


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)

class User(BaseModel):
    name:str = Field(min_length=2)
    age:int = Field(gt=0,lt=120)
    email: EmailStr
    is_employed: bool
    address:Address

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only letters')
        return value



    @model_validator(mode='before')
    @classmethod
    def check_age(cls, values):
        age = values.get('age')
        is_employed = values.get('is_employed')
        if is_employed and (age < 18 or age > 65):
            raise ValueError('Employed users must be between 18 and 65 years old')
        return values

def check_json(data_json):
    try:
        user = User.model_validate_json(data_json)
        print("Валидация json прошла успешно")
        return user.model_dump_json(indent=4)
    except ValidationError as e:
            return f'Ошибка валидации: {e.json()}'

json_input = """{
    "name": "John",
    "age": 63,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""
try:
    user = check_json(json_input)
    print(user)
except ValidationError as e:
    print(f'Ошибка валидации край: {e.json()}')
