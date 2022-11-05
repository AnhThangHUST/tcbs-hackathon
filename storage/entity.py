from datetime import date

from sqlalchemy import BigInteger, Column, Text, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DocumentEntity(Base):
    __tablename__ = 'data_raw'

    id = Column(BigInteger, primary_key=True)
    url = Column(Text)
    title = Column(Text)
    description = Column(Text)
    body = Column(Text)
    source_type = Column(Text)


class SynonymEntity(Base):
    __tablename__ = 'dictionary'

    id = Column(BigInteger, primary_key=True)
    word = Column(Text)
    synonym = Column(Text)


class HistoryEntity(Base):
    __tablename__ = 'history'

    id = Column(BigInteger, primary_key=True)
    data_raw_id = Column(BigInteger)
    tcbsid = Column(Text)
    create_date = Column(Date)
