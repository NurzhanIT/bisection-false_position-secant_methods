def bisection(function, n1, n2, lim):
    res = 0

    if function(n1) * function(n2) >= 0:
        return print("Not valid values")

    condition = n2 - n1
    while n2 - n1 >= lim:

        res = (n1 + n2) / 2

        if function(res) == 0:
            break
        if function(res) * function(n1) < 0:
            n2 = res
        else:
            n1 = res

    print(round(res, str(lim).count("0")))
