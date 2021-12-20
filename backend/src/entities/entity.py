# coding=utf-8
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

db_url = 'localhost:5432'
db_name = 'online-exam'
db_user = 'postgres'
db_password = '0NLIN3-ex4m'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity():
    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    created_at = Column(DateTime)

    def __init__(self):
        self.uuid = str(uuid.uuid1())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
