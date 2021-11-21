import numpy as np
import matplotlib.pyplot as plt
import os

# Read in points from text file
path = os.path.abspath(os.getcwd())
directory = path + '\\Homework 3\\hw03_pca_data.txt'
points = np.loadtxt(directory)

# Calculate mean
mean = np.mean(points, axis=0)
print("The mean vector of the dataset: " + str(mean))

# Calculate covarience
data = points - mean
covariance = np.matmul(data, data.T)
print("The covariance matrix of the dataset: " + str(covariance))

# Calculate eigenvalues/eigenvectors
eigvals, eigvecs = np.linalg.eig(covariance)
print("The eigenvalues of the covariance matrix are: " + str(eigvals))
print("The eigenvectors of the covariance matrix are: " + str(eigvecs))
