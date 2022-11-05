from storage import session
from storage.entity import DocumentEntity, SynonymEntity

default_page_size = 100


def getAllDocument():
    res = []
    page_index = 0

    move_next = True
    while move_next:
        query_res = session.query(DocumentEntity).limit(default_page_size).offset(page_index * default_page_size).all()
        page_index += 1
        if len(query_res) == 0:
            move_next = False
    return res


def getDocumentWithPagination(page_index, page_size):
    query_res = session.query(DocumentEntity).limit(page_size).offset(page_index * page_size).all()
    return query_res


def getAllSynonym():
    return session.query(SynonymEntity).all()
