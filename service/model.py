import json


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


class DocumentDataResponse:
    def __init__(self, document):
        self.title = document.title
        self.description = document.description
        self.link = document.url

    def __repr__(self):
        return json.dumps(self.__dict__)


class SearchResponse:
    def __init__(self, document):
        self.source = document.source_type
        self.data = DocumentDataResponse(document)
