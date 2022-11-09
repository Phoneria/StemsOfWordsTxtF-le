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
file_name = "bigBadWords"

my_file = open(file_name + ".txt", "r")

text = my_file.read()
tokens = word_tokenize(text)
lemma_function = WordNetLemmatizer()

my_set = {""}
for token, tag in pos_tag(tokens):
    lemma = lemma_function.lemmatize(token, tag_map[tag[0]])

    if (lemma != token):
        a = token + " => " + lemma
        my_set.add(a)

my_list = list(my_set)
my_list.sort()

with open(file_name + "_words_changed.txt", 'w', encoding='utf-8') as f:
    for i in my_list:
        f.write(i + "\n")

my_set = {""}
for token, tag in pos_tag(tokens):
    lemma = lemma_function.lemmatize(token, tag_map[tag[0]])

    a = token + " => " + lemma
    my_set.add(a)

my_list = list(my_set)
my_list.sort()

with open(file_name + "_words_all.txt", 'w', encoding='utf-8') as f:
    for i in my_list:
        f.write(i + "\n")



