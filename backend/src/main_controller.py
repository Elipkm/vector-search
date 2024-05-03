import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import gensim.downloader as api
from search_in_elastic import searchElasticKnn
from vector_to_elastic import writeVectorToElastic
from folder_to_vector import getVectorDocuments

app = Flask(__name__)
CORS(app) 

word2vec_model = api.load("word2vec-google-news-300")
indexName = "full_vector_search"
language = "english"

@app.route('/index_folder', methods=['POST'])
def endpoint1():
    data = request.json 
    if 'path' in data:
        path = data['path']
        # Process the data...
        documentsVectors = getVectorDocuments(path, language, word2vec_model)

        writeVectorToElastic(documentsVectors, indexName)

        result = {'message': "Received data at endpoint 1 with value: {path}"}
        return jsonify(result)
    else:
        return jsonify({'error': 'Key not found in request data'}), 400

@app.route('/search', methods=['POST'])
def endpoint2():
    data = request.json  
    if 'searchterm' in data:
        searchterm = data['searchterm']
        # Process the data...
        searchResult = searchElasticKnn(searchterm, indexName=indexName, aiModel=word2vec_model, language=language)
        return jsonify(searchResult)
    else:
        return jsonify({'error': 'Key not found in request data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
