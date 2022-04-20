# mehdi shahsavari 98235025

import numpy as np

W = 10000
L = 4
I = 3.25 * 10**-4
E = 2 * 10 ** 11

let = int(24*E*I)
const = round(W/let, 8)

X = float(input("please enter a float number as X: "))


def result(arq):
    for arq in np.arange(0, 0.5):
        Y = const * (X**4 - 4*L*(X**3) + 6*(L**2)*(X**2))
        return Y


print("Deflection is: ", result(X))
