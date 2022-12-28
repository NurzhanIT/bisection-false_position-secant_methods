import bisection_algorithm
import math


def function(x):
    return pow(x, 10)-1


n1 = 0
n2 = 10
lim = 0.001

bisection_algorithm.bisection(function, n1, n2, lim)
