from sqlalchemy import BigInteger, Text, create_engine, Column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine(
    'postgresql://postgres:1234@127.0.0.1:5432/postgres',
    echo=True
)

# engine = create_engine('postgresql://postgres:Hanoi2022@34.135.118.24:5432/crawler',
#                        connect_args={'connect_timeout': 30}, echo=True)
try:
    engine.connect()
    print("success")
except SQLAlchemyError as err:
    raise RuntimeError('can not connect to database')

session = sessionmaker(bind=engine)()
page_size = 100


class DocumentEntity(Base):
    __tablename__ = 'data_raw'

    id = Column(BigInteger, primary_key=True)
    url = Column(Text)
    title = Column(Text)
    description = Column(Text)
    body = Column(Text)
    source_type = Column(Text)


class Document:
    id = 0
    url = ""
    title = ""
    description = ""
    body = ""
    source_type = ""

    def __init__(self, documentEntity):
        self.id = documentEntity.id
        self.url = documentEntity.body
        self.title = documentEntity.title
        self.description = documentEntity.description
        self.body = documentEntity.body
        self.source_type = documentEntity.source_type


class SynonymEntity(Base):
    __tablename__ = 'dictionary'

    id = Column(BigInteger, primary_key=True)
    word = Column(Text)
    synonym = Column(Text)


def getAllDocument():
    res = []
    page_index = 0

    move_next = True
    while move_next:
        query_res = session.query(DocumentEntity).limit(page_size).offset(page_index * page_size).all()
        page_index += 1
        if len(query_res) == 0:
            move_next = False
        for r in query_res:
            res.append(Document(r))
    return res

def createThesaurus():
    query_res = session.query(SynonymEntity).all()
    thesaurus = {}
    for r in query_res:
        r.synonym.replace(" ", "")
        words = r.synonym.split(",")
        words.append(r.word)
        words_set = set(words)
        for w in words:
            if w not in thesaurus:
                thesaurus[w] = words_set
            else:
                thesaurus[w] = thesaurus[w].union(words_set)
    return thesaurus


global_thesaurus = createThesaurus()
