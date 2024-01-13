from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/mydatabase"
Base = declarative_base()

class Nutritionist(Base):
    __tablename__ = 'nutritionists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(String)
    telegram_nick = Column(String)

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    complaints = Column(String)
    diet = Column(String)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def save_nutritionist(data):
    session = Session()
    nutritionist = Nutritionist(...)
