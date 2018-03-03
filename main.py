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

#print(sym.pi)
train(42)
ind = 0
point = []
# Creates an array with all the features of the given
# data point. The -1 index of 'point' is the label
for k in range(number_of_features):
    point.append(testing_labels[k][57])

print(point)
print(neural_network(point,network_weights,bias))
point = []

for k in range(number_of_features):
    point.append(testing_labels[k][66])

print(point)
print(neural_network(point,network_weights,bias))

print("--- %s seconds ---" % (time.time() - start_time))