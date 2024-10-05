from numpy import array


# Ket 0 and Ket 1 represented as arrays in python
ket0 = array([1, 0])
ket1 = array([0, 1])

print(ket0 / 2 + ket1 / 2)

# We can also use arrays to create matrices that represent operations
M1 = array([1,1], [0, 0])
M2 = array([1, 1], [1, 0])

print(M1 / 2 + M2 / 2)
