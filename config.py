from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///user_db.db',connect_args={'check_same_thread': False})
# Base.metadata.bind = engine
# Base.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)
session = DBsession()