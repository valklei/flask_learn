from sqlalchemy import (
    Integer,
    BigInteger,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship
)

from VK_1 import engine, Base

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(20)
    )
    surname: Mapped[str] = mapped_column(
        String(25),
        default="No Surname", # на стороне ORM
        server_default="No Surname"
    )

    addresses: Mapped['Address'] = relationship(
        'Address',
        back_populates='user'
    )
    profile: Mapped['Profile'] = relationship(
        'Profile',
        back_populates='user',
        uselist=False)

class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    city: Mapped[str] = mapped_column(
        String(20)
    )
    country: Mapped[str] = mapped_column(
        String(30),
        unique=True
    )
    street: Mapped[str] = mapped_column(
        String(40)
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('users.id')
    )

    user: Mapped['User'] = relationship(
        'User',
        back_populates='addresses'
    )


class Profile(Base):
    __tablename__ = 'profile'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    email: Mapped[str] = mapped_column(
        String(75),
        unique=True
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('users.id'),
        unique=True
    )

    user: Mapped['User'] = relationship(
        'User',
        back_populates='profile'
    )

Base.metadata.create_all(bind=engine)
