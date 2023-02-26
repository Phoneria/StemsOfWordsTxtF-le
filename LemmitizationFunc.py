import nltk

"""
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
"""
import string
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict


def stem(text):
    tag_map = defaultdict(lambda: wn.NOUN)
    tokens = word_tokenize(text)
    lemma_function = WordNetLemmatizer()

    for i in nltk.pos_tag(tokens):
        if (i[1] == "POS" or i[1] == "MD" or i[1] == "CD" or i[1] == "PRP" or i[1] == "CC"
                or i[1] == "TO" or i[1] == "IN" or i[1] == "DT" or i[1] == "WRB" or i[1] == "WDT" or i[1] == "PRP$" or
                i[1] == "WP"):
            tokens.remove(i[0])

    my_dict = {}
    for token, tag in pos_tag(tokens):
        my_dict[token] = lemma_function.lemmatize(token, tag_map[tag[0]])

    new_dict = my_dict.copy()

    for i in my_dict.keys():
        if i in string.punctuation:
            new_dict.pop(i)

        if i.isdigit():
            new_dict.pop(i)

    my_dict = new_dict

    # return list(my_dict)
    return my_dict

"""
my_file = open("sample.txt", "r", encoding='utf-8')
text = my_file.read()
print(stem(text))
my_file.close()
"""