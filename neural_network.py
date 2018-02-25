# This file defines the neural network function
# that will be used to make predictions

from sigmoid import *
from initialize_data import *

# Define neural network with input lists features, weights,
# the bias term, and return the network's prediction
def neural_network(features, weights, bias):
    # This is the output, or prediction, of the neural network
    prediction = 0

    # The -1 index of list 'features' is actually the
    # label, and not a feature, thus it is skipped
    for i in range(len(features)-1):
        prediction += features[i] * weights[i]
    prediction += bias
    return sig(prediction)