import false_position_method


def function(x):
    return x * x * x - 5 * x + 1


n1 = -9
n2 = 10
decimal = 3

false_position_method.false_position(function, n1, n2, decimal)
