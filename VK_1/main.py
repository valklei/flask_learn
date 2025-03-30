from models_relations import User
from db_connection import DBConnection

from VK_1 import engine

user = User(id=1, name="Dima")

with DBConnection(engine) as session:
    session.add(user)
    session.commit()
