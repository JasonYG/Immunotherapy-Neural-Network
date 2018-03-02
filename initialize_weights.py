# This file creates all the initial weights for
# the neural network given the features dataset

# Import data from other file
from initialize_data import *

import numpy as np

network_weights = []

for i in range(number_of_features):
    # Start with random values for weights
    v = np.random.randn()
    network_weights.append(v)

bias = np.random.randn()