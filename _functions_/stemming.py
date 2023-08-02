from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem import PorterStemmer

factory = StemmerFactory()

ps = PorterStemmer()
ss = factory.create_stemmer()


def stem(string_list, stem_language):
    res = []
    if stem_language == "1":
        for word in string_list:
            res.append(ss.stem(word))
    elif stem_language == "2":
        for word in string_list:
            res.append(ps.stem(word))
    return res