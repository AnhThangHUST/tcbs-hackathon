from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql://postgres:1234@127.0.0.1:5432/postgres',
    echo=True
)

# engine = create_engine('postgresql://postgres:Hanoi2022@34.135.118.24:5432/crawler',
#                        connect_args={'connect_timeout': 30}, echo=True)
try:
    engine.connect()
    print("connect to database success")
except SQLAlchemyError as err:
    raise RuntimeError('can not connect to database')

Session = sessionmaker(bind=engine)
session = Session()
