
import json
from elasticsearch import Elasticsearch
import numpy
import gensim.downloader as api
from service.preprocess import preprocess_text
from service.textToToken import getVectorsFromTextPreload


def searchElasticKnn(searchterm, indexName, aiModel, language="english"):
    preprocessText = preprocess_text(searchterm, language)
    vectors = getVectorsFromTextPreload(preprocessText, aiModel)

    # connect by an api key
    es = Elasticsearch(hosts="http://localhost:9200", api_key="UkFkM1BvOEIzTVNtR09QX0lDVGk6VDBoemtDcFZReXFzQ2p5OWhCaDFvdw==")
    print("search vector array")
    vectors = numpy.array(vectors).tolist()[0]
    vectorQuery = {
        "knn": {
            "field": "content_vector",
            "query_vector": vectors,
            "num_candidates": 100
        }
    }
    # search 
    resp = es.search(index=indexName, query=vectorQuery, source=False, fields=["filename"])

    return resp.body["hits"]

