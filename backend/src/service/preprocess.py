import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK resources (stopwords and tokenizers)
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text, language='english'):
    # Tokenize text
    tokens = word_tokenize(text, language=language)
    
    # Lowercase all tokens
    tokens = [token.lower() for token in tokens]
    
    # Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    
    # Remove stopwords
    stop_words = set(stopwords.words(language))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back into a single string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

# Example French text
#text = "The Evolution of Rock and Blues Fusion: Rock and blues music have a rich history of intertwining and evolving together, creating a unique fusion that has shaped the music industry for decades. This fusion emerged in the early to mid-20th century when blues artists like Muddy Waters and Howlin' Wolf influenced rock pioneers such as Chuck Berry and Elvis Presley. These early rockers adopted the raw emotion and soulful expression of blues music, infusing it with electrifying guitar riffs and energetic rhythms. As rock and blues continued to evolve, artists like Jimi Hendrix and Led Zeppelin pushed the boundaries even further, incorporating elements of psychedelia and heavy metal into the mix. This fusion reached new heights in the 1970s with the rise of blues-rock bands like The Allman Brothers Band and Cream, who blurred the lines between genres with their virtuosic performances and improvisational jams. Today, the influence of rock and blues fusion can be heard in a wide range of musical styles, from classic rock to modern indie bands, proving that this dynamic partnership continues to inspire artists and audiences alike."

# Preprocess the text in French
#preprocessed_text = preprocess_text(text, language='english')
#print("Original text:", text)
#print("Preprocessed text:", preprocessed_text)
