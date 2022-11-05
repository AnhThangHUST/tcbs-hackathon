from service import document_crud
from service.model import SearchResponse
from storage import repository_executor

def getHistotyOfTcbsId(tcbsid):
    query_res = repository_executor.getHistoryByTcbsId(tcbsid)
    idsDataRow = []
    for r in query_res:
        idsDataRow.append(r.data_raw_id)

    document = document_crud.getDocumentWhereIdIn(idsDataRow)

    filteredIWC = filter(lambda data: data.source_type == 'iwealth_club', document)
    filteredTCIV = filter(lambda data: data.source_type == 'tcinvest', document)

    result = [filteredIWC[0:5], filteredTCIV[0:5]]

    return [SearchResponse(d) for d in result]


def insertHistory(drawDataId, tcbsid):
    repository_executor.insertHistory(drawDataId, tcbsid)
    return "ok"
