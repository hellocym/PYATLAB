# pyatlab.py (Python 3 version)
# Matlab functions in python
# Started in 2020/02/29
# created by Harry Chen (CYMIC)

import math
import numpy as np
import scipy.sparse


def linspace(d1, d2, n=100):
    n = float(n)
    n1 = math.floor(n) - 1
    c = (d2 - d1) * (n1 - 1)
    if math.isinf(c):
        y = [d1 + x * ((d2 / n1) - (d1 / n1)) for x in range(n1 + 1)]
    else:
        y = [d1 + x * (d2 - d1) / n1 for x in range(n1 + 1)]
    y[0] = d1
    y[-1] = d2
    return y


# print(linspace(1, 4, 5))


def logspace(d1, d2, n=50):
    # n = float(n)

    if d2 == math.pi or d2 == math.pi:
        d2 = math.log10(d2)
    if n < 1:
        y = []
    else:
        y = [10 ** (d1 + x * (d2 - d1) / (math.floor(n) - 1)) for x in range(n - 1)] + [10 ** d2]
    return y


# print(logspace(0, math.log10(32), 6))


def isempty(d):
    if d:
        return False
    else:
        return True


def isscalar(d):
    if (type(d) == int) or (type(d) == bool) or (type(d) == float) or (type(d) == complex):
        return True
    elif (type(d) == list) and (len(d) == 1):
        return True
    elif (type(d) == np.ndarray) and (d.shape == (1, 1)):
        return True
    else:
        return False


def isvector(d):
    if (type(d) == list):
        return True
    elif (type(d) == np.ndarray) and ((d.shape[0] == 1) or (d.shape[1] == 1)):
        return True
    else:
        return False


def issparse(d):
    return isspars(d)


# A = 32
# print(isscalar(A))
# B = [x for x in range(1, 6)]
# print(isvector(B))
# print(isempty(B))
