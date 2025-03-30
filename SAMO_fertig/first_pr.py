from typing import Optional
from sqlalchemy import (
    create_engine,
    Integer,
    String,
    ForeignKey, Float, Boolean)
from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker)

engine = create_engine("sqlite:///first_pr.db", echo=True, echo_pool=True)
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[str] = mapped_column(String(50))
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.close()
