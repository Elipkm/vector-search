
from elasticsearch import Elasticsearch

def createMyIndex(esClient,indexName):

    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "description": {"type": "text"},
                "timestamp": {"type": "date"}
            }
        }
    }
    esClient.indices.create(index=indexName, body=index_settings)


def writeVectorToElastic(myVectors, indexName):
    es = Elasticsearch(hosts="http://localhost:9200", api_key="UkFkM1BvOEIzTVNtR09QX0lDVGk6VDBoemtDcFZReXFzQ2p5OWhCaDFvdw==")
    # setup elastic search
    if es.indices.exists(index=indexName) == False:
        createMyIndex(es, indexName)
    # Index a document
    for myVector in myVectors:
        print("index: " + myVector.get("filename"))
        es.index(index=indexName, body=myVector)


