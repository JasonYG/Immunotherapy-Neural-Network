# This file trains the neural network by updating the
# weights based on the squared error cost function

# Import code from other files
from initialize_weights import *

import numpy as np
import sympy as sym

# Defines train function, which takes in an integer 'n',
# which represents the number of training feature data points
def train(n):
    # The value of this variable is arbitrary, and can be
    # changed to yield better results from the neural network
    number_of_loops = 1000
    for i in range(number_of_loops):
        ind = np.random.randint(n)
        point = []

        # Creates an array with all the features of the given
        # data point. The -1 index of 'point' is the label
        for k in range(number_of_features):
            point.append(training_labels[k][ind])

       # label = point[-1]

        # Updates the weights of each feature
        for k in range(number_of_features-1):
            # The label of the data point can be either 0 or 1
            #NEXT: define neural network function, take partial derivatives of weights
            #prediction = neuralnetwork(point[k])
            print("hello world")