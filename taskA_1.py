import bisection_algorithm


def function(x):
    return x * x * x - x - 1


n1 = -9
n2 = 10
lim = 0.001

bisection_algorithm.bisection(function, n1, n2, lim)
