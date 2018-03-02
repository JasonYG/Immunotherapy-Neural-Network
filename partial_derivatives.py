# This files take the partial derivatives of the squared
# error cost function with respect to all of the parameters,
# i.e. the weights of the neural network

# Import code from other files
from initialize_weights import *

import sympy as sym

# Defines function that takes in a list of features as its
# argument and returns a list of the partial derivatives of
# the cost function
def differentiate(point):
    # The -1 index of 'point' is the label
    label = point[-1]

    # Squared error cost
    cost = (prediction - label) ** 2

    # Intermediary term
    z = 0
    for i in range(len(network_weights)-1):
        z += point[i] * network_weights[i]
        Take partial derivatives


