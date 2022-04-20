import numpy as np

# all zero values
arr = np.zeros((2, 3))
print(arr)

# all one values
arr1 = np.ones((4, 5))
print(arr1)

# all other types value
arr2 = np.full((3, 7), 24)
print(arr2)

# creating array
arr3 = np.array([1, 4, 5, 6, 7])
arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr3)
print(arr4)

# get specific value
x = arr3[2]
y = arr4[0, 3]
print(x)
print(y)

# get specific row
z = arr4[0, :4]
print(z)

# get specific column
t = arr4[:, 3]
print(t)

# random decimal numbers
r = np.random.rand(4, 5)
print(r)

# random integer numbers (100 means that the maximum value is 100 )(min = -10, max = 10)
h = np.random.randint(100, size=(3, 3))
g = np.random.randint(-10, 10, size=(4, 4))
print(h)
print(g)

# repeat an array
arr5 = np.array([[1, 2, 3]])
r1 = np.repeat(arr5, 3, axis=0)
print(r1)

# problem
output = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:4, 1:4] = z
print(output)

# mathematic
a = np.array([1, 2, 3, 4])
print(a)
b = a + 2
print(b)
c = a * 4
print(c)

d = np.array([6, 7, 8, 9])
e = a + d
print(e)

# take the sin
k = np.sin(a)
n = np.cos(d)
print(k)
print(n)

# linear algebra
am = np.ones((2, 3))
bm = np.full((3, 2), 2)

cm = np.matmul(am, bm)
print(cm)

# find the determinant
hm = np.identity(3)
print(hm)
fm = np.linalg.det(hm)
print(fm)

arr6 = np.array([[1, 4, 73], [2, 500, 8], [34, 6, 9]])
darr6 = np.linalg.det(arr6)
print(darr6)

# statics
nf = np.min(arr6)
db = np.max(arr6)
sm = np.sum(arr6)
print(nf)
print(db)
print(sm)


# reorganizing Array

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((2, 2, 2))
print(after)

# Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

v = np.vstack([v1, v2, v1, v2])
print(v)

# Horizontal  stack
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

hd = np.hstack((h1, h2))
print(hd)
