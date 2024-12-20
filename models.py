from sqlalchemy import Column, Integer, String

from config import Base

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key = True)
    email = Column(String(30), nullable=True)
    username = Column(String(20), unique = True, nullable= True)
    password = Column(String(20), nullable= True)
    