# This files take the partial derivatives of the squared
# error cost function with respect to all of the parameters,
# i.e. the weights of the neural network

# Import code from other files
from initialize_weights import *
from neural_network import *

import sympy as sym

# Defines function that takes in a list of features as its
# argument and returns a list of the partial derivatives of
# the cost function
def differentiate(point):
    # This will be the output of the function
    partials = []

    # The -1 index of 'point' is the label
    label = point[-1]

    # Prediction from neural network
    prediction = neural_network(point, network_weights, bias)

    # Create the 'weight symbols', which will be used
    # to represent the variables in the cost equation
    weight_symbols = []
    # Represents the bias term
    b = sym.symbols('b')
    for i in range(len(network_weights)):
        symbol = 'w' + str(i)
        symbol = sym.symbols(symbol)
        weight_symbols.append(symbol)

    # Adds all the network weights and bias to the prediction,
    # which then goes into the sigmoid function
    pred = 0
    for i in range(len(network_weights)):
        pred += weight_symbols[i] * network_weights[i]
    pred += b

    # Take sigmoid of the prediction
    sig = 1/(1+sym.exp(-pred))
    #print(sig)

    # Final cost function
    f_cost = (sig-label)**2
    #print(len(network_weights))
    # Take partial derivative of final cost function
    # with respect to all the weights
    for i in range(len(network_weights)+ 1):
        # The -1 index of the output will be the
        # partial with respect to the bias term
        if (i == len(network_weights)):
            alg_dcost_dweight = sym.diff(f_cost, b)
        # Algebraic expression for derivative
        else:
            alg_dcost_dweight = sym.diff(f_cost, weight_symbols[i])
        alg_dcost_dweight = alg_dcost_dweight.subs(b, bias)

        # Simplified number for derivative
        simp_dcost_dweight = alg_dcost_dweight.subs({weight_symbols[j]:network_weights[j] for j in range(len(network_weights))})

        answer = simp_dcost_dweight.evalf()
        partials.append(answer)
    # Take partial derivative of final cost function
    # with respect to the bias term
    #print(partials)
    #for i in range(len(network_weights)-1):
    return partials



