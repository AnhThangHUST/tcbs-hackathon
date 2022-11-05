import json

from flask import Flask, app, request

from service import document_crud, search_engine
from util import datastructure_util

server = Flask(__name__)


@server.route('/hello')
def helloWorld():
    return 'Hello World!'


@server.route('/test-db')
def testDb():
    return datastructure_util.serializeList(document_crud.getDocumentWithPagination(0, 10))


@server.route('/index-data')
def indexData():
    document_crud.indexAllDocuments()
    return "index data done"


@server.route('/search')
def search():
    term = request.args.get("term")
    tcbsId = request.args.get("tcbsId")
    response = search_engine.search(term, tcbsId)
    return json.loads(datastructure_util.serializeList(response))


@server.route('/history', methods=['GET'])
def getHistoryByTcbsId():
    tcbsid = request.args.get('tcbsid')
    response = document_crud.getHistotyOfTcbsId(tcbsid)
    return json.loads(datastructure_util.serializeList(response))


@server.route('/history', methods=['POST'])
def insertTcbsId():
    tcbsid = request.args.get('tcbsid')
    drawDataId = request.args.get('drawDataId')
    response = document_crud.insertHistory(drawDataId, tcbsid)
    return datastructure_util.serializeList(response)


if __name__ == '__main__':
    server.run(host='127.0.0.1', port=8888, debug=True, ssl_context='adhoc')
