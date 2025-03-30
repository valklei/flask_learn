from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from Connector import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")