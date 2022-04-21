# mehdi shahsavari 98235025

import numpy as np

W = 10000
L = 4
I = 3.25 * 10**-4
E = 2 * 10 ** 11

let = int(24*E*I)
const = round(W/let, 8)
limit = np.arange(0, 0.5, 0.00000001)
print(limit)
X = float(input("please enter a float number as X: "))


def arrange(args):
    if args in limit:
        Y = float(const * (args**4 - 4*L*(args**3) + 6*(L**2)*(args**2)))
        return Y
    else:
        print("not in range")


print("Deflection is: ", arrange(X))
