# This file trains the neural network by updating the
# weights based on the squared error cost function

# Import code from other files
from initialize_weights import *
from partial_derivatives import *

import numpy as np
import sympy as sym

# Defines train function, which takes in an integer 'n',
# which represents the number of training feature data points
def train(n):
    global bias
    # The value of these variable is arbitrary, and can be
    # changed to yield better results from the neural network
    number_of_loops = 100
    learning_rate = 0.1
    for i in range(number_of_loops):
        ind = np.random.randint(n)
        point = []
        # Creates an array with all the features of the given
        # data point. The -1 index of 'point' is the label
        for k in range(number_of_features):
            point.append(training_labels[k][ind])

        # List containing all the partial derivatives of the cost
        # function with respect to the weights and bias of the
        # neural network, to be used in updating the weights

        update_weights = differentiate(point)

        # Updates the weights of each feature
        for k in range(number_of_features-1):
            network_weights[k] -= learning_rate * update_weights[k]
        # Updates the bias term
        bias -= learning_rate * update_weights[-1]
    return