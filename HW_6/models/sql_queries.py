from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import db

class Queries(db.Model):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True)
    text = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="queries")


