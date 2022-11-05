from service import document_crud
from service.model import SearchResponse
from storage import repository_executor
from storage.entity import HistoryEntity


def getHistotyOfTcbsId(tcbsid):
    query_res = repository_executor.getHistoryByTcbsId(tcbsid)
    idsDataRow = []
    for r in query_res:
        history = HistoryEntity(r)
        idsDataRow.append(history.data_raw_id)
    return [SearchResponse(d) for d in document_crud.getDocumentWhereIdIn(idsDataRow)]


def insertHistory(drawDataId, tcbsid):
    repository_executor.insertHistory(drawDataId, tcbsid)
    return "ok"
