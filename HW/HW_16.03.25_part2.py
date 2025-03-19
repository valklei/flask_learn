from pydantic import BaseModel, EmailStr
class User(BaseModel):
    username: str
    email: EmailStr
    def __str__(self):
        return f"User {self.username}, Email: {self.email}"
class AdminUser(User):
    access_level: int = 10  # Предоставляем более высокий уровень доступа по умолчанию
    def __str__(self):
        return f"Admin {self.username}, Email: {self.email}, Access Level: {self.access_level}"

    def promote_user(self, user: User):
        print(f"Promoting {user.username} to higher privileges")

        return AdminUser(username=user.username, email=user.email, access_level=self.access_level+1)

user = User(username="Vlad", email="test.email@gmail.com")
user1 = User(username="Valerii", email="valerii@gmail.com")
admin = AdminUser(username="Alex", email="admin@gmail.com")
print(admin)
promoted_user = admin.promote_user(user)
promoted_user1 = admin.promote_user(user1)
print(promoted_user)
print(promoted_user1)