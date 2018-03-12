# INTRODUCTION HERE

# Import code from other files
from initialize_data import *
from initialize_weights import *
from training_loop import *
from sigmoid import *
from neural_network import *
from partial_derivatives import *

# Import dependencies
import sympy as sym
import time
start_time = time.time()

# Train neural network
train(45)

# Test neural network
accuracy = 0
for j in range(45, 90):
    # Creates an array with all the features of the given
    # data point. The -1 index of 'point' is the label
    point = []
    for k in range(number_of_features):
      point.append(testing_labels[k][j])
    pred = neural_network(point,network_weights,bias)
    print(point)
    print("Result for " + str(j) + " is: " + str(pred) + "\n")
    if round(pred) == point[-1]:
        accuracy += 1
print("The accuracy of the neural network is: " + str(accuracy/45 * 100) + "%")
print("--- %s seconds ---" % (time.time() - start_time))