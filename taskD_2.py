import secant_method
import math

def function(x):
    return x*x*x+x*x+x+7


n1 = -2.5
n2 = 0
lim = 0.001

secant_method.secant(function, n1, n2, lim)
