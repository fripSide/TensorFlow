# coding: utf-8
__author__ = 'fripSide'

import pickle
import tensorflow as tf
import numpy as np


dataset = None

with open("save.pickle", "rb") as fp:
    dataset = pickle.load(fp)

test_size = int(len(dataset) * 0.1)

dataset = np.array(dataset)


