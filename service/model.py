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
