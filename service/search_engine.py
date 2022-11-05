from service import embed_batch_text, global_thesaurus, elasticsearch_client, document_crud
from service.model import SearchResponse
from config import tcinvest_config_indexed_by_url


def search(term, tcbsId):
    if term is None:
        documents = document_crud.getHistotyOfTcbsId(tcbsId)
    else:
        print("start search with term ", term)
        text_list = tokenizeText(term)
        text_vector_list = embed_batch_text(text_list)
        response = searchMatchWholePhrase(text_list)
        # searchByCosineSimilarity(text_vector_list)
        document_ids = []
        for hit in response["hits"]["hits"]:
            document_ids.append(hit["_source"]["document_id"])

        documents = document_crud.getDocumentWhereIdIn(document_ids)
    res = []
    for d in documents:
        searchResponse = SearchResponse(d)
        if d.source_type == 'tcinvest':
            if d.url in tcinvest_config_indexed_by_url:
                detail_cfg = tcinvest_config_indexed_by_url[d.url]
                searchResponse.data.
                searchResponse.data.title = detail_cfg.get("title")
                searchResponse.data.icon = detail_cfg.get("icon")
                searchResponse.data.routingUrl = detail_cfg.get("routingUrl")
                searchResponse.data.roles = detail_cfg.get("roles")
                searchResponse.data.viewType = detail_cfg.get("viewType")
                searchResponse.data.description = detail_cfg.get("description")
        res.append(searchResponse)
    return res


def tokenizeText(text):
    text = " ".join(text.lower().split())
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
