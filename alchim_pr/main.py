
from model_relations import User
from db_connection import DBConnection

from sqlalchemy_train import engine

user = User(...)

with DBConnection(engine) as session:
    session.add(user)
