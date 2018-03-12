# This file defines the sigmoid function, which maps the
# output of the neural network to a number between 0 and
# 1
import math
def sig(x):
    try:
        return 1/(1+math.exp(-x))
    except OverflowError:
        if x > 0:
            return 0
        else:
            return 1