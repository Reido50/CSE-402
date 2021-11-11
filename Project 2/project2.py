import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal
import scipy
import math
import os
import sys
import csv
import copy

import scipy

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

def CalcOrientationField(filename):
    path = os.path.abspath(os.getcwd())
    img = Image.open(path + '\\Project 2\\proj02_q1_fingerprint_images\\' + filename).convert('L')
    img_mat = np.matrix(img)
    # Apply sobel filters
    sobel_x = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]]).T
    sobel_y = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]]).T
    G_x = signal.convolve2d(img_mat, sobel_x, 'valid')
    G_y = signal.convolve2d(img_mat, sobel_y, 'valid')
    # Pad G_x and G_y with 0s on the border
    G_x = np.pad(G_x, pad_width=1, mode='constant', constant_values=0)
    G_y = np.pad(G_y, pad_width=1, mode='constant', constant_values=0)
    # Calculate orientation field
    orientationField = [[0]*len(G_x[0])]*len(G_x)
    for x in range(4, len(G_x)-4):
        for y in range(4, len(G_x[0])-4):
            sum_numerator = 0
            sum_denomenator = 0
            for i in range(-4, 4):
                for j in range(-4, 4):
                    sum_numerator += 2 * G_x[x+i][y+j] * G_y[x+i][y+j]
                    sum_denomenator += (G_x[x+i][y+j]**2) - (G_y[x+i][y+j]**2)
            orientationField[x][y] = (math.pi / 2) + 0.5 * math.atan2(sum_numerator, sum_denomenator)
    # Write to CSV File
    np.savetxt("orientationField" + filename + ".csv",
            orientationField,
            delimiter =", ",
            fmt ='% s')

def MinutiaeMatcher(p, q):
    C = np.zeros((len(p), len(q), 4))
    
    for i in range(len(p)):
        for j in range(len(q)):
            # Compute transformation parameters
            tx = q[j][0] - p[i][0]
            ty = q[j][1] - p[i][1]
            tr = math.radians(q[j][2] - p[i][2])
            # Apply transformation to all points in M_1 and determine if point is in tolerance
            p_p = copy.deepcopy(p)
            for k in range(len(p)):
                p_p[k][0] = (p[k][0]-p[i][0])*math.cos(tr) + (p[k][1]-p[i][1])*math.sin(tr) + (p[i][0] + tx)
                p_p[k][1] = -(p[k][0]-p[i][0])*math.sin(tr) + (p[k][1]-p[i][1])*math.cos(tr) + (p[i][1] + ty)
                min_dist = 10.0
                for l in range(len(q)):
                    dist = abs(math.dist((p_p[k][0], p_p[k][1]), (q[l][0], q[l][1])))
                    if dist < min_dist:
                        min_dist = dist
                        C[i][j][0] = tx
                        C[i][j][1] = ty
                        C[i][j][2] = tr
                if min_dist != 10.0:
                    C[i][j][3] += 1
    # Find the max C value
    maxVal = -1
    maxLoc = [0,0]
    for x in range(len(C)):
        for y in range(len(C[0])):
            if C[x][y][3] > maxVal:
                maxVal = C[x][y][3]
                maxLoc = [x,y]
    # Return transformation params and number of matching pairs
    return C[maxLoc[0]][maxLoc[1]]

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

'''
# QUESTION 2
# Ridge Pattern Wave
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

# QUESTION 3
# Calculate Orientation Field
CalcOrientationField('user001_1.gif')
CalcOrientationField('user002_1.gif')
CalcOrientationField('user003_1.gif')
CalcOrientationField('user004_1.gif')
CalcOrientationField('user005_1.gif')
CalcOrientationField('user006_1.gif')
CalcOrientationField('user007_1.gif')
CalcOrientationField('user008_1.gif')
CalcOrientationField('user009_1.gif')
CalcOrientationField('user010_1.gif')
'''

# QUESTION 4
# Extract data
path = os.path.abspath(os.getcwd())
directory = path + '\\Project 2\\proj02_q2_minpoints\\'
filenames = []
minpoints = []
for filename in os.listdir(directory):
    f = open(directory + filename)
    temp = []
    for line in f.readlines():
        point = []
        for num in line.split():
            point.append(float(num))
        temp.append(point)
    minpoints.append(temp)
    filenames.append(filename)
# Calculate all combinations and print
for i in range(len(minpoints)):
    for j in range(len(minpoints)):
        match_data = MinutiaeMatcher(minpoints[i], minpoints[j])
        print("%s %1s %4d %4d %10.6f %4d" % 
            (filenames[i], filenames[j], match_data[0], 
            match_data[1], match_data[2], match_data[3]))   
