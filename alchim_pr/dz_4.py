from sqlalchemy import create_engine, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker, joinedload

engine = create_engine("sqlite:///:memory:", echo=True, echo_pool=True)
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    products: Mapped["Product"] = relationship("Product", back_populates="category")


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
session.close()


category_list = [
    Category(name="Электроника;", description="Гаджеты и устройства."),
    Category(name="Книги", description="Печатные книги и электронные книги."),
    Category(name="Одежда", description="Одежда для мужчин и женщин.")]

session.add_all(category_list)
session.commit()

product_list = [
    Product(name="Смартфон", price=299.99, in_stock=True, category_id=category_list[0].id),
    Product(name="Ноутбук", price=499.99, in_stock=True, category_id=category_list[0].id),
    Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category_id=category_list[1].id),
    Product(name="Джинсы", price=40.50, in_stock=True, category_id=category_list[2].id),
    Product(name="Футболка", price=20.00, in_stock=True, category_id=category_list[2].id)]






session.add_all(product_list)
session.commit()


categories = session.query(Category).options(joinedload(Category.products)).all()

# Вывод результатов
for category in categories:
    print(f"Category: {category.name}")
    if category.products:
        for product in category.products:
            print(f" - Product: {product.name}, Price: {product.price}")
    else:
        print(" - No associated products")

session.close()