from service import embed_batch_text, global_thesaurus, elasticsearch_client, document_crud
from service.model import SearchResponse
from config import tcinvest_config_indexed_by_url

crawler_source = ["tcinvest", "tcbs", "iwealth_club"]
result_per_group = 5


def search(term, tcbsId):
    if term is None:
        documents = document_crud.getHistoryOfTcbsId(tcbsId)
    else:
        print("start search with term ", term)
        text_list = tokenizeText(term)
        text_vector_list = embed_batch_text(text_list)
        m1 = searchMatchWholePhrase(text_list)
        m2 = searchByCosineSimilarity(text_vector_list)
        m1 = joinSearchResult(m1, m2)
        document_ids = []
        for v in m1.values():
            for document_id in v:
                document_ids.append(document_id)
        documents = document_crud.getDocumentWhereIdIn(document_ids)

    group_documents = {}
    for d in documents:
        if d.source_type not in group_documents:
            group_documents[d.source_type] = []
        group_documents[d.source_type].append(d)

    res = []

    for source, ds in group_documents.items():
        searchResponse = SearchResponse(source, ds)
        if source == 'tcinvest':
            for i, d in enumerate(searchResponse.data):
                if d.routingUrl in tcinvest_config_indexed_by_url:
                    detail_cfg = tcinvest_config_indexed_by_url[d.routingUrl]
                    searchResponse.data[i].title = detail_cfg.get("title")
                    searchResponse.data[i].icon = detail_cfg.get("icon")
                    searchResponse.data[i].routingUrl = detail_cfg.get("routingUrl")
                    searchResponse.data[i].roles = detail_cfg.get("roles")
                    searchResponse.data[i].viewType = detail_cfg.get("viewType")
                    searchResponse.data[i].description = detail_cfg.get("description")
                    searchResponse.data[i].type = detail_cfg.get("type")
            res.insert(0, {"source": source, "data": searchResponse.data})
        else:
            res.append({"source": source, "data": searchResponse.data})
    return res


def tokenizeText(text):
    text = " ".join(text.lower().split())
    text_list = [text]
    # for word in global_thesaurus.keys():
    #     if word in text:
    #         for synonym in global_thesaurus[word]:
    #             text_list.append(text.replace(word, synonym))

    return text_list


def searchMatchWholePhrase(text_list):
    text = text_list[0]
    m = {}

    for cs in crawler_source:
        script_query = {"bool": {"must": [
            {
                "match": {
                    "sentence": {
                        "query": text,
                        "operator": "AND"
                    }
                }
            }, {
                "match_phrase": {
                    "source": {
                        "query": cs,
                    }
                }
            }
        ]}}

        response = execSearch(script_query)
        m[cs] = []
        for hit in response["hits"]["hits"]:
            m[cs].append(hit["_source"]["document_id"])
        m[cs] = list(set(m[cs]))

    return m


def searchByCosineSimilarity(text_vector_list):
    # text_vector = text_vector_list[0]
    text_vector = text_vector_list[0]

    m = {}

    for cs in crawler_source:
        script_query = {
            "script_score": {
                "query": {
                    "match_phrase": {
                        "source": {
                            "query": cs,
                        }
                    }
                },
                "script": {
                    "source": "cosineSimilarity(params.vector, 'sentence_vector') + 1.0",
                    "params": {"vector": text_vector}
                }
            }
        }
        response = execSearch(script_query)
        m[cs] = []
        for hit in response["hits"]["hits"]:
            if hit["_score"] >= 1.6:
                m[cs].append(hit["_source"]["document_id"])
        m[cs] = list(set(m[cs]))

    return m


def execSearch(script_query):
    return elasticsearch_client.search(
        index='hackathon',
        body={
            "size": 5,
            "query": script_query,
            "_source": {
                "includes": ["document_id", "sentence"]
            },
        },
        ignore=[400]
    )


def joinSearchResult(m1, m2):
    for k, v1 in m1.items():
        if len(v1) < result_per_group:
            for e in m2[k]:
                v1.append(e)
                if len(v1) == result_per_group:
                    break
            m1[k] = v1
    return m1
