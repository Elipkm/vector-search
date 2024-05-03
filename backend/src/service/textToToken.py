import gensim.downloader as api

def getVectorsFromTextSAV(text):
    # Load pre-trained Word2Vec model
    word2vec_model = api.load("word2vec-google-news-300")

    # Generate document embeddings
    document_embeddings = []
    words = text.split(" ")
    word_embeddings = [word2vec_model[word] for word in words if word in word2vec_model]
    if word_embeddings:
        doc_embedding = sum(word_embeddings) / len(word_embeddings)  # Average of word embeddings
        document_embeddings.append(doc_embedding)
    else:
        document_embeddings.append(0)  # Handle cases where no embeddings are found

    # Now, you can use document_embeddings for indexing and semantic search
    return document_embeddings


def getVectorsFromTextPreload(text, word2vec_model):
    # Generate document embeddings
    document_embeddings = []
    words = text.split(" ")
    word_embeddings = [word2vec_model[word] for word in words if word in word2vec_model]
    if word_embeddings:
        doc_embedding = sum(word_embeddings) / len(word_embeddings)  # Average of word embeddings
        document_embeddings.append(doc_embedding)
    else:
        document_embeddings.append(0)  # Handle cases where no embeddings are found

    # Now, you can use document_embeddings for indexing and semantic search
    return document_embeddings


