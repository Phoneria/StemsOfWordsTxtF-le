import nltk

"""
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
"""

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict

tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV


def stem(text):

    tokens = word_tokenize(text)
    lemma_function = WordNetLemmatizer()

    my_set = {""}
    for token, tag in pos_tag(tokens):
        my_set.add(lemma_function.lemmatize(token, tag_map[tag[0]]))
        

    my_list = list(my_set)
    my_list.sort()
    my_list.remove('')
    
    return my_list

stem("Sample text will be here")

