import json
import os
import sys
import numpy

from service.preprocess import preprocess_text
from service.textToToken import getVectorsFromTextPreload

def isTextFile(filename):
    return filename.endswith('.txt')

def getVectorDocuments(folderPath, language, aiModel):
    print("folderPath: " + folderPath)
    print("language: " + language)

    # List all files in the directory
    results = []
    filenames = os.listdir(folderPath)
    textFilenames = list(filter(lambda filename: isTextFile(filename), filenames))
    print("found " + str(len(textFilenames)) + " text files")
    i = 0
    for filename in textFilenames:
        # Open the file
        filepath = os.path.join(folderPath, filename)
        with open(filepath, 'r') as file:
            text = file.read()
            preprocessText = preprocess_text(text, language)
            vectors = getVectorsFromTextPreload(preprocessText, aiModel)

            result = {
                "filename": filename,
                "content_vector": numpy.array(vectors).tolist()[0]
            }
            results.append(result)
            i += 1
            print("processed file " + str(i) + " of " + str(len(textFilenames)))
    print(results)
    return results
