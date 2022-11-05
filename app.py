import json

from flask import Flask, request

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
    response = search_engine.search(term)
    return json.loads(datastructure_util.serializeList(response))


if __name__ == '__main__':
    server.run(host='127.0.0.1', port=8888, debug=True)
