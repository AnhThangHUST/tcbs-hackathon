from storage import session
from storage.entity import DocumentEntity, SynonymEntity, HistoryEntity

default_page_size = 100


def getAllDocument():
    res = session.query(DocumentEntity).filter(DocumentEntity.source_type == "tcinvest").all()
    # page_index = 0
    #
    # move_next = True
    # while move_next:
    #     query_res = session.query(DocumentEntity).limit(default_page_size).offset(page_index * default_page_size).all()
    #     page_index += 1
    #     if len(query_res) == 0:
    #         move_next = False
    return res


def getDocumentWithPagination(page_index, page_size):
    query_res = session.query(DocumentEntity).limit(page_size).offset(page_index * page_size).all()
    return query_res


def getDocumentWhereIdIn(ids):
    query_res = session.query(DocumentEntity).where(DocumentEntity.id.in_(ids)).all()
    return query_res


def getAllSynonym():
    return session.query(SynonymEntity).all()


def insertHistory(dataDrawId, tcbsid):
    history = HistoryEntity(
        data_raw_id=dataDrawId,
        tcbsid=tcbsid)
    session.add(history)
    session.commit()


def getHistoryByTcbsId(tcbsid):
    query_res = session.query(HistoryEntity).filter(HistoryEntity.tcbsid == tcbsid).all()
    return query_res
