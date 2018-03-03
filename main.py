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

#print(sym.pi)
point = []
for k in range(number_of_features):
    point.append(training_labels[k][0])
differentiate(point)