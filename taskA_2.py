import bisection_algorithm
import math


def function(x):
    return x - math.cos(x)


n1 = -9
n2 = 10
lim = 0.001

bisection_algorithm.bisection(function, n1, n2, lim)
