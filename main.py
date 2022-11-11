from sympy import *

from sympy.stats import *

import numpy as np

from math import ceil, e, pi, exp

import random

random.seed(100)

x = Symbol('x')
n = Symbol('n')

# my_functions = [x**0, x, x**2, sin(x), e**x, e**(2*x), e**(3*x), e**(4*x), sin(2*x), sin(3*x), sin(4*x), x**3,
# x**4, x**5, x**6, x**7, x**8]

my_functions = []
for i in range(20):
    my_functions.append((x ** i).evalf())
my_functions.append(cos(x))


my_data = []
for i in range(100):
    val = random.uniform(-3, 3)
    #my_data.append((val, density(Normal("normal", 0, 2))(val).evalf() + random.random()))
#    my_data.append((val, (1/(2*pi)**0.5)*e**((-1/2)*val**2)+random.uniform(-0.1, 0.1)))
    my_data.append((val, cos(val)+random.uniform(-0.1, 0.1)))
print(my_data)


def sigmoid(val):
    return 1/(1+exp(val))


def split_data(data, split=0.1):
    testing_size = ceil(len(data) * split)
    test = []
    for i in range(testing_size):
        rand = random.randint(0, len(data) - 1)
        test.append(data[rand])
        del data[rand]
    return data, test


def optimize(train, test, functions):
    best_funcs = []
    for f in range(len(functions)):
        variances = {}
        for f_ in functions:
            variances[f_] = variance(test, least_squares(train, best_funcs+[f_]))
        if best_funcs:
            if min(variances.values()) >= variance(test, least_squares(train, best_funcs)):
                # print(min(variances.values()))
                # print(variance(test, least_squares(train, best_funcs)))
                # print(variances)
                return least_squares(train, best_funcs)
        best_funcs.append(min(variances, key=variances.get))
        functions.remove(min(variances, key=variances.get))


def variance(data, func):
    ret = 0
    for i in range(len(data)):
        ret += (data[i][1] - func.subs(x, data[i][0])) ** 2
    return float(ret / (len(data) - 1))


def least_squares(data, functions):
    A = np.zeros((len(data), len(functions)))

    y = np.zeros((len(data), 1))

    for k in range(len(functions)):
        for i in range(len(data)):
            func = functions[k]
            A[i, k] = func.subs(x, data[i][0])
            y[i, 0] = data[i][1]

    x_hat = np.matmul(np.linalg.inv(np.matmul(np.transpose(A), A)), np.matmul(np.transpose(A), y))
    ret = 0
    for i in range(len(functions)):
        ret += float(x_hat[i]) * functions[i]
    return ret


def least_squares_multivariate(data, functions):
    A = np.zeros((len(data), len(functions)))

    y = np.zeros((len(data), 1))

    for k in range(len(functions)):
        for i in range(len(data)):
            func = functions[k]
            A[i, k] = func.subs(x, data[i][0])
            y[i, 0] = data[i][1]

    x_hat = np.matmul(np.linalg.inv(np.matmul(np.transpose(A), A)), np.matmul(np.transpose(A), y))
    ret = 0
    for i in range(len(functions)):
        ret += float(x_hat[i]) * functions[i]
    return ret


if __name__ == '__main__':
    training, testing = split_data(my_data)
    val = optimize(training, testing, my_functions)
    print(val)
#    print(variance(testing, val))
