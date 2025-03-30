from Connector import engine, Base, session
from Category import Category
from Product import Product

Base.metadata.create_all(engine)

category_electronics = Category(name="Электроника", description="Гаджеты и устройства.")
category_books = Category(name="Книги", description="Печатные книги и электронные книги.")
category_clothing = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add_all([category_electronics, category_books, category_clothing])
session.commit()

categories = session.query(Category).all()

for category in categories:
    parent_id= category.parent_id if category.parent_id else "None"
    print(f"Category: {category.name}, Description: {category.description}, Parent: {parent_id}")

products = session.query(Product).all()
product_smartphone = Product(name="Смартфон", price=299.99, in_stock=True, category_id=category_electronics.id)
product_laptop = Product(name="Ноутбук", price=499.99, in_stock=True, category_id=category_electronics.id)
product_book = Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category_id=category_books.id)
product_jeans = Product(name="Джинсы", price=40.50, in_stock=True, category_id=category_clothing.id)
product_tshirt = Product(name="Футболка", price=20.00, in_stock=True, category_id=category_clothing.id)

session.add_all([product_smartphone, product_laptop, product_book, product_jeans, product_tshirt])
session.commit()

for product in products:
    print(f"Product: {product.name}, Price: {product.price}, In Stock: {product.in_stock}, Category: {product.category.name}")