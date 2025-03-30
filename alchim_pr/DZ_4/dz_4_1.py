from sqlalchemy import create_engine, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker, joinedload
from sqlalchemy.orm import aliased
from sqlalchemy import func


engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    in_stock: Mapped[bool] = mapped_column(Boolean)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship("Category", back_populates="products")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Добавление категорий
category_list = [
    Category(name="Электроника", description="Гаджеты и устройства."),
    Category(name="Книги", description="Печатные книги и электронные книги."),
    Category(name="Одежда", description="Одежда для мужчин и женщин.")
]

session.add_all(category_list)
session.commit()

# Добавление продуктов
product_list = [
    Product(name="Смартфон", price=299.99, in_stock=True, category_id=category_list[0].id),
    Product(name="Ноутбук", price=499.99, in_stock=True, category_id=category_list[0].id),
    Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category_id=category_list[1].id),
    Product(name="Джинсы", price=40.50, in_stock=True, category_id=category_list[2].id),
    Product(name="Футболка", price=20.00, in_stock=True, category_id=category_list[2].id)
]

session.add_all(product_list)
session.commit()

# Запрос категорий с продуктами
categories = session.query(Category).options(joinedload(Category.products)).all()

# Вывод результатов
for category in categories:
    print(f"Category: {category.name}")
    if category.products:
        print('*' * 50)
        for product in category.products:

            print(f" - Product: {product.name}, Price: {product.price}")
        print('*'*50)
    else:
        print(" - No associated products")



    # 3 Найти первый продукт с названием "Смартфон"

    smartphone = session.query(Product).filter_by(name="Смартфон").first()

    # Обновить цену продукта
    if smartphone:
        smartphone.price = 349.99
        session.commit()
        print('*'*50)
        print(f"Updated price for {smartphone.name} to {smartphone.price}")
        print('*'*50)
    else:
        print("Product 'Смартфон' not found.")




# 4. Задача 4: Агрегация и группировка
# Подсчитаем общее количество продуктов в каждой категории.



# Подсчет количества продуктов в каждой категории
category_counts = (
    session.query(
        Category.name, func.count(Product.id)
    )
    .outerjoin(Product, Category.id == Product.category_id)
    .group_by(Category.id)
    .all()
)

# Вывод результатов
print('*' * 50)
for category_name, product_count in category_counts:

    print(f"Category: {category_name}, Product Count: {product_count}")
print('*'*50)


# Задача 5: Группировка с фильтрацией
# Выведем только те категории, в которых более одного продукта

# Фильтрация категорий с более чем одним продуктом
categories_with_multiple_products = (
    session.query(Category.name)
    .join(Product, Category.id == Product.category_id)
    .group_by(Category.id)
    .having(func.count(Product.id) > 1)
    .all()
)

# Вывод результатов
for category_name, in categories_with_multiple_products:
    print('*' * 50)
    print(f"Category with more than one product: {category_name}")
    print('*'*50)



session.close()
