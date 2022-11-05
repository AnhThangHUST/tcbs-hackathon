from elasticsearch.helpers import bulk

from service import elasticsearch_client, tokenizer, embed_batch_text
from service.model import Document
from storage import repository_executor
from util import datastructure_util


def getDocumentWithPagination(page_index, page_size):
    query_res = repository_executor.getDocumentWithPagination(page_index, page_size)
    return [Document(q) for q in query_res]


def getDocumentWhereIdIn(ids):
    query_res = repository_executor.getDocumentWhereIdIn(ids)
    return [Document(q) for q in query_res]


def indexAllDocuments():
    index_name = "hackathon"
    elasticsearch_client.indices.delete(index=index_name, ignore=[404])
    entities = repository_executor.getAllDocument()
    for entity in entities:
        document = Document(entity)
        indexSentencesFromOneDocument(document, index_name)
    print("indexing all documents done")


# test index sentence
def indexSentencesFromOneDocument(document, index_name):
    raw_sentences = tokenizer.tokenize(". ".join([document.title, document.body, document.description]))
    sentences = []
    for sentence in raw_sentences:
        sentence = datastructure_util.processSentence(sentence)
        if len(sentence) == 0 or sentence.startswith("image"):
            continue
        sentences.append(sentence)

    requests = []
    content_vectors = embed_batch_text(sentences)
    for i, sentence in enumerate(sentences):
        request = {
            "_index": index_name,
            "document_id": document.id,
            "sentence": sentence,
            "vector": content_vectors[i]
        }
        requests.append(request)

    print("start bulk elastic search ", document.id)
    bulk(elasticsearch_client, requests)
    print("bulk success ", document.id)
