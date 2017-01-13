# coding: utf-8
__author__ = 'fripSide'

import numpy as np
import tensorflow as tf
import random
import pickle
from collections import Counter

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

pos_file = "pos.txt"
neg_file = "neg.txt"


def create_lexicon(pos_file, neg_file):
    lexs = []

    def process_file(f):
        with open(f, 'r') as fp:
            lex = []
            for line in fp.readlines():
                words = word_tokenize(line.lower())
                lex += words
            return lex

    lexs += process_file(pos_file)
    lexs += process_file(neg_file)
    lemmatizer = WordNetLemmatizer()
    lexs = [lemmatizer.lemmatize(word) for word in lexs]

    word_count = Counter(lexs)
    lexs = []
    for word in word_count:
        if 2000 > word_count[word] > 20:
            lexs.append(word)

    return lexs

# 保存文本中出现的单词
lexs = create_lexicon(pos_file, neg_file)


# 讲单词转换成向量
def normalize_dataset(lex):
    dataset = []

    def string_to_vector(lex, line, clf):
        words = word_tokenize(line.lower())
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]

        features = np.zeros(len(lex))
        for word in words:
            if word in lex:
                features[lex.index(word)] = 1
        return [features, clf]


    def add_to_dateset(f, clf):
        with open(f, "r") as fp:
            for line in fp.readlines():
                one_sample = string_to_vector(lex, line, clf)
                dataset.append(one_sample)

    add_to_dateset(pos_file, [1, 0])
    add_to_dateset(neg_file, [0, 1])
    return dataset


dataset = normalize_dataset(lexs)
random.shuffle(dataset)

with open("save.pickle", "wb") as fp:
    pickle.dump(dataset, fp)

