from msilib.schema import BindImage
from os import name
from sqlalchemy import Engine
from models import Base, User


Base.metadata.create_all(Engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(BindImage = Engine)
session = Session()

for item in data: # type: ignore
    user = User(id-item['id'], name-item['name'])
    session.add(user)
    
session.commit()