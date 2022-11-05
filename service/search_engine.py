from service import embed_batch_text, global_thesaurus, elasticsearch_client, document_crud
from service.model import SearchResponse
from config import tcinvest_config_indexed_by_url


def search(term):
    if term is None:
        return ["Cuong implement here"]

    print("start search with term ", term)
    text_list = tokenizeText(term)
    text_vector_list = embed_batch_text(text_list)
    response = searchMatchWholePhrase(text_list)
    # searchByCosineSimilarity(text_vector_list)
    document_ids = []
    for hit in response["hits"]["hits"]:
        document_ids.append(hit["_source"]["document_id"])

    res = []
    for d in document_crud.getDocumentWhereIdIn(document_ids):
        searchResponse = SearchResponse(d)
        if d.source_type == 'tcinvest':
            if d.url in tcinvest_config_indexed_by_url:
                detail_cfg = tcinvest_config_indexed_by_url[d.url]
                searchResponse.data.title = detail_cfg["title"]
                searchResponse.data.icon = detail_cfg["icon"]
                searchResponse.data.routingUrl = detail_cfg["routingUrl"]
                searchResponse.data.roles = detail_cfg["roles"]
                searchResponse.data.viewType = detail_cfg["viewType"]
                searchResponse.data.description = detail_cfg["description"]
    return res


def tokenizeText(text):
    text_list = [text]
    for word in global_thesaurus.keys():
        if word in text:
            for synonym in global_thesaurus[word]:
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
