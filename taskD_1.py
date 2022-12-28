import secant_method
import math

def function(x):
    return x-math.exp(-x)


n1 = 0
n2 = 10
lim = 0.001

secant_method.secant(function, n1, n2, lim)
