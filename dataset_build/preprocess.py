from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer as wnl
import re

def normalize(text: str)->str:
    text = text.lower()
    token_words=word_tokenize(text)
    norm_text = []
    for word in token_words:
        if not any(i.isdigit() for i in word):
            norm_text.append(word)
    return " ".join(norm_text)

def removeUnicodeChar(text: str)->str:
    text = text.replace('-', ' ')
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    return text

def removeStopWords(text: str):
    stop = stopwords.words('english')
    text = " ".join([word for word in word_tokenize(text) if word not in stop])
    return text

def lemmSentence(text: str):
    lem = wnl()
    token_words=word_tokenize(text)
    res = ''
    for word in token_words:
        lemmed = lem.lemmatize(word=word)
        res += lemmed+' '
    return res.rstrip()

def appendBiGram(text: str):
    res = ''
    token_words=word_tokenize(text)
    for x in zip(*[token_words[i:] for i in range(2)]):
        res += ('_'.join(x)+' ')
    text += ' '+res.rstrip()
    return text

def preprocess_tokenize(text: str)->list:
    res = list()
    text = normalize(text)
    text = removeUnicodeChar(text)
    text = removeStopWords(text)
    text = lemmSentence(text)
    text = appendBiGram(text)
    res.extend(word_tokenize(text))
    return res