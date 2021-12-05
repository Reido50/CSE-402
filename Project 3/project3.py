import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageFilter
from scipy import signal
import scipy
import math
import os
import sys
import csv
import copy

def ShowBrightenImage(img, value):
    return ImageEnhance.Brightness(img).enhance(value)

def ShowContrastedImage(img, value):
    return ImageEnhance.Contrast(img).enhance(value)

def ShowGuassianImage(img, value):
    return img.filter(ImageFilter.GaussianBlur)

def ComputeLBP(img_mat):
    indexOffsetDict = {0:(-1, -1), 1:(0, -1), 2:(1, -1),
                   3:(1, 0), 4:(1, 1), 5:(0, 1),
                   6:(-1, 1), 7:(-1, 0)}

    padded = np.pad(img_mat, pad_width=1, mode='constant', constant_values=0)
    LBP_img = np.zeros(img_mat.shape)
    for x in range(1, len(padded) - 1):
        for y in range(1, len(padded[0]) - 1):
            bin_str = ''
            for i in range(8):
                cur_ind = (indexOffsetDict[i][1] + x, indexOffsetDict[i][0] + y)
                center = padded[x][y]
                compare = padded[cur_ind[0]][cur_ind[1]]
                if center > compare:
                    bin_str += str(0)
                else:
                    bin_str += str(1)
            bin_str = bin_str[::-1]
            print(str(x) + ", " + str(y) + " " + str(bin_str))

# Question 1
# (a)
filename = 'face_grey.jpg'
path = os.path.abspath(os.getcwd())
img = Image.open(path + '\\Project 3\\' + filename)
img_mat = np.array(img)
brightened = ShowBrightenImage(img, 1.5)
contrasted = ShowContrastedImage(img, 1.5)
guassian = ShowGuassianImage(img, 1.5)
'''
brightened.show()
contrasted.show()
guassian.show()
'''

# (b)
test_mat = np.matrix([[5, 3, 2], [6, 3, 2], [4, 4, 1]])
print(test_mat)
ComputeLBP(test_mat)
