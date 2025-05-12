from pydantic import (Field, EmailStr, field_validator,  model_validator, ValidationError, HttpUrl)
from pydantic import BaseModel

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    def __str__(self):
        return f"User {self.username}, Email: {self.email}"

class AdminUser(User):
    access_level: int = 10 # Предоставляем более высокий уровень доступа по умолчанию
    def __str__(self):
        return f"Admin {self.username}, Email: {self.email}, Access Level:{self.access_level}"


    def promote_user(self, user: User):
        print(f"Promoting {user.username} to higher privileges")
        return AdminUser(username=user.username, email=user.email,
        access_level=self.access_level + 1)
# Пример использования
# Создание объекта пользователя
user = User(username='john_doe', email='john.doe@example.com')
print(user)
# Создание объекта администратора и продвижение пользователя
admin = AdminUser(username='admin_user', email='admin@example.com')
print(admin)
promoted_user = admin.promote_user(user)
print(promoted_user)