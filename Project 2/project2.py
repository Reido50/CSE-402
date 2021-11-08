import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal
import math
import os
import sys

indexDict = {0:(1,2), 1:(0,2), 2:(0,1),
             3:(0,0), 4:(1,0), 5:(2,0),
             6:(2,1), 7:(2,2)}

def PoincareIndex(theta):
    if theta > 90:
        return theta - 180
    elif theta < -90:
        return theta + 180
    else:
        return theta

def DecodeOrientationField(m):
    sumation = 0
    for i in range(8):
        index = indexDict[i]
        nextIndex = indexDict[(i+1) % 8]
        theta = m[nextIndex[0]][nextIndex[1]] - m[index[0]][index[1]]
        sumation += PoincareIndex(theta)
    result = sumation / 180
    if result == 0:
        return "non-singularity"
    elif result == 1:
        return "loop"
    elif result == -1:
        return "delta"
    elif result == 2:
        return "whorl"
    return None

def PlotRidgePattern(x, y, A, theta, f):
    # Instantiate image
    image = [[(0,0,0)]*x]*y

    # Calculate pixel intensities
    for i in range(len(image)):
        for j in range(len(image[0])):
            intensity =  (int)(A * math.cos(2*math.pi*f*(i*math.cos(theta)+j*math.sin(theta))))
            image[i][j] = (intensity, intensity, intensity)

    # Setting axes
    fig = plt.figure()
    # Plot the functions
    plt.imshow(image)
    # Title
    plt.title("Ridge Pattern (x=" + str(x) + ", y=" + str(y) + ", A=" + str(A) + ", theta=" + str(math.degrees(theta)) + ", f=" + str(f) + ")")
    # Show the plot
    plt.show()

# QUESTION 1
# Orientation Field Calculations
# 1
field1 = [[10, 15, -10],
            [12, 0, 15],
            [13, 12, -5]]
print("Field 1 is a " + DecodeOrientationField(field1))
# 2
field2 = [[45, 90, -50],
          [50, 0, -45],
          [5, 0, -5]]
print("Field 2 is a " + DecodeOrientationField(field2))
# 3
field3 = [[50, 0, -50],
          [75, 0, -70],
          [85, 90, -85]]
print("Field 3 is a " + DecodeOrientationField(field3))
# 4
field4 = [[45, 2, -50],
          [90, 0, 90],
          [-50, 2, 50]]
print("Field 4 is a " + DecodeOrientationField(field4))

# QUESTION 2
# Ridge Pattern Wave
'''
PlotRidgePattern(600, 600, 80, math.radians(0), 0.01)
PlotRidgePattern(600, 600, 80, math.radians(45), 0.01)
PlotRidgePattern(600, 600, 80, math.radians(90), 0.01)
PlotRidgePattern(600, 600, 80, math.radians(135), 0.01)
PlotRidgePattern(600, 600, 160, math.radians(0), 0.01)
PlotRidgePattern(600, 600, 160, math.radians(45), 0.01)
PlotRidgePattern(600, 600, 160, math.radians(90), 0.01)
PlotRidgePattern(600, 600, 160, math.radians(135), 0.01)
PlotRidgePattern(600, 600, 80, math.radians(0), 1)
PlotRidgePattern(600, 600, 80, math.radians(45), 1)
PlotRidgePattern(600, 600, 80, math.radians(90), 1)
PlotRidgePattern(600, 600, 80, math.radians(135), 1)
PlotRidgePattern(600, 600, 80, math.radians(0), 10)
PlotRidgePattern(600, 600, 80, math.radians(45), 10)
PlotRidgePattern(600, 600, 80, math.radians(90), 10)
PlotRidgePattern(600, 600, 80, math.radians(135), 10)
'''

# QUESTION 3
# Calculate Orientation Field
path = os.path.abspath(os.getcwd())
img = Image.open(path + '\\Project 2\\proj02_q1_fingerprint_images\\user001_1.gif').convert('L')


sobel_x = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])
sobel_y = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
G_x = signal.convolve2d(img, sobel_x)
G_y = signal.convolve2d(img, sobel_y)
orientationField = [[0]*img.size[1]]*img.size[0]
for x in range(img.size[0]):
    for y in range(img.size[1]):
        sum_numerator = 0
        sum_denomenator = 0
        for i in range(-4, 4):
            for j in range(-4, 4):
                sum_numerator += 2 * G_x[x+i][y+i] * G_y[x+i][y+i]
                sum_denomenator += (G_x[x+i][y+j]**2) - (G_y[x+i][y+j]**2)
        orientationField[x][y] = 0.5 * math.atan2(sum_numerator, sum_denomenator)
