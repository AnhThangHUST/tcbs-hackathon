from flask import Flask

import document_repo
import search_engine
from util import datastructure_util

server = Flask(__name__)


@server.route('/hello')
def helloWorld():
    return 'Hello World!'


@server.route('/test-db')
def testDb():
    search_engine.indexAllDocuments()
    return datastructure_util.serializeList(document_repo.getAllDocument())
    # return search_engine.search("đầu tư")


@server.route('/index-data')
def indexData():
    search_engine.indexAllDocuments()
    return "index data done"


@server.route('/search')
def search():
    search_engine.search("Kết nối")
    return "search done"


if __name__ == '__main__':
    server.run(host='127.0.0.1', port=8888, debug=True)
