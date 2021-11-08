import numpy as np
import matplotlib.pyplot as plt

# Create column vector a
a = np.random.rand(10)
print("a: " + str(a) + "\n")

# Create column vector b that is related to a
b = a**3 + a**2 + a + 5
print("b: " + str(b) + "\n")

# Plot (a,b)
fig = plt.figure()
plt.scatter(a, b)
plt.show()

# Multiply a with the transpose of b
product = a * b.T
print("a * b.T: " + str(product) + "\n")

# Inverse of a maitrx
nums = np.matrix([[1, 2, 5],
                  [5, 5, 8],
                  [6, 4, 1]])
nums_inv = np.linalg.inv(nums)
print("Inverse of nums: " + str(nums_inv) + "\n")

# eigen vectors and eigen values of a matrix
eigvals, eigvecs = np.linalg.eig(nums)
print("Eigenvalues of nums: " + str(eigvals))
print("Eigenvectors of nums: " + str(eigvecs) + "\n")

# Number of times a certain values appears
fives = np.count_nonzero(nums == 5)
print("Number of 5s in nums: " + str(fives) + "\n")


