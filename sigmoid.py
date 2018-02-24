# This file defines the sigmoid function, which maps the
# output of the neural network to a number between 0 and
# 1
import math
def sig(x):
    return 1/(1+math.exp(-x))