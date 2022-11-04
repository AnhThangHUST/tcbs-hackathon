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


if __name__ == '__main__':
    server.run(host='127.0.0.1', port=8888, debug=True)