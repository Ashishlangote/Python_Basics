from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

userid = 'root'
pwd = 'ashish'
my_db = 'orm'

connection_str = f'mysql+pymysql://{userid}:{pwd}@localhost/{my_db}'
# mysql+pymysql://<username>:<password>@<host>/<dbname>

Base = declarative_base()
engine = create_engine(connection_str, echo=True)
session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    sid = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f'User username = {self.username}, email = {self.email}'
