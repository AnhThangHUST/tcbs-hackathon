import json


class Document:
    def __init__(self, documentEntity):
        self.id = documentEntity.id
        self.url = documentEntity.url
        self.title = documentEntity.title
        self.description = documentEntity.description
        self.body = documentEntity.body
        self.source_type = documentEntity.source_type


class DocumentDataResponse:
    def __init__(self, document):
        self.id = document.id
        self.title = document.title
        self.description = document.description
        self.routingUrl = document.url
        self.viewType = ""
        self.isOpenNewTab = True
        self.roles = []
        self.icon = ""

    def __repr__(self):
        return json.dumps(self.__dict__)


class SearchResponse:
    def __init__(self, source, documents):
        self.source = source
        self.data = [DocumentDataResponse(document) for document in documents]
