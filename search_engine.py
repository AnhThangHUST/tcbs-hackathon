import nltk.data
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from pyvi.ViTokenizer import tokenize
from sentence_transformers import SentenceTransformer

import document_repo
from util import datastructure_util

elasticsearch_client = Elasticsearch()
model_embedding = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
nltk.data.path.append("/home/thangna/hackathon/nltk_data")
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')


def embed_batch_text(batch_text):
    batch_embedding = model_embedding.encode(batch_text)
    return [vector.tolist() for vector in batch_embedding]


def indexAllDocuments():
    index_name = "hackathon"
    elasticsearch_client.indices.delete(index=index_name, ignore=[404])
    documents = document_repo.getAllDocument()
    for document in documents:
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


# todo search per group
def search(text):
    text_list = tokenizeText(text)
    text_vector_list = embed_batch_text(text_list)
    response = searchMatchWholePhrase(text_list)
    # searchByCosineSimilarity(text_vector_list)
    for hit in response["hits"]["hits"]:
        print (hit["_source"]["document_id"])



def tokenizeText(text):
    text_list = [text]
    for word in document_repo.global_thesaurus.keys():
        if word in text:
            for synonym in document_repo[word]:
                text_list.append(text.replace(word, synonym))

    return text_list


def searchMatchWholePhrase(text_list):
    script_query = {"bool": {"should": []}}
    for text in text_list:
        script_query["bool"]["should"].append({
            "match": {
                "sentence": {
                    "query": text,
                    "operator": "AND"
                }
            }
        })

    return execSearch(script_query)


def searchByCosineSimilarity(text_vector_list):
    script_query = {
        "script_score": {
            "query": {
                "match_all": {}
            }
            ,
            "script": {
                "source": "cosineSimilarity(params.sentence_vector, 'sentence_vector') + 1.0",
                "params": {"sentence_vector": text_vector_list}
            }
        }
    }

    return execSearch(script_query)


def execSearch(script_query):
    return elasticsearch_client.search(
        index='hackathon',
        body={
            "size": 10,
            "query": script_query,
            "_source": {
                "includes": ["document_id", "sentence"]
            },
        },
        ignore=[400]
    )
