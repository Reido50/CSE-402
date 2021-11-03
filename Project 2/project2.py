import numpy as np
import matplotlib.pyplot as plt
import math
import os

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
    return sumation / 180

