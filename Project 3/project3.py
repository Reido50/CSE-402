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
            int_rep = int(bin_str, 2)
            LBP_img[x-1][y-1] = int_rep
    return LBP_img

def CompareImgMat(im1, im2):
    sum_diff = 0
    for x in range(len(im1)):
        for y in range(len(im1[0])):
            sum_diff += abs(im1[x][y] - im2[x][y])
    return sum_diff / (len(im1) * len(im1[0]))

# Question 1
# (a)
filename = 'face_grey.jpg'
path = os.path.abspath(os.getcwd())
img = Image.open(path + '\\Project 3\\' + filename)
Fo = np.matrix(img.convert('L'))
Fb = ShowBrightenImage(img, 1.5)
Fc = ShowContrastedImage(img, 1.5)
Fg = ShowGuassianImage(img, 1.5)
'''
Fb.show()
Fc.show()
Fg.show()
Fb.save(path + '\\Project 3\\bright.jpg')
Fc.save(path + '\\Project 3\\contrasted.jpg')
Fg.save(path + '\\Project 3\\guassian.jpg')
'''

# (b)
Lo = ComputeLBP(np.array(img.convert('L')))
Lb = ComputeLBP(np.array(Fb.convert('L')))
Lc = ComputeLBP(np.array(Fc.convert('L')))
Lg = ComputeLBP(np.array(Fg.convert('L')))
'''
plt.imshow(grey_arr, 'gray')
plt.show()
plt.imshow(gray_LBP_arr, cmap='gray')
plt.show()
plt.imshow(bright_LBP_arr, cmap='gray')
plt.show()
plt.imshow(contrast_LBP_arr, cmap='gray')
plt.show()
plt.imshow(gaussian_LBP_arr, cmap='gray')
plt.show()
'''
# (c)
print("Lo vs Lb:" + str(CompareImgMat(Lo, Lb)))
print("Lo vs Lc:" + str(CompareImgMat(Lo, Lc)))
print("Lo vs Lg:" + str(CompareImgMat(Lo, Lg)))
# (d)
print("Fo vs Fb:" + str(CompareImgMat(np.array(Fo), np.array(Fb))))
print("Fo vs Fc:" + str(CompareImgMat(np.array(Fo), np.array(Fc))))
print("Fo vs Fg:" + str(CompareImgMat(np.array(Fo), np.array(Fg))))

# Question 2
faces = np.zeros((50, 30, 30))
directory = path + '\\Project 3\\proj03_face_images\\'
i = 0
for filename in os.listdir(directory):
    cur_img = Image.open(directory + filename).convert('L')
    faces[i] += np.array(cur_img)
    i += 1
# (a)
first30 = np.zeros((30, 30, 30))
i = 0
for sub in range(10):
    for f in range(3):
        first30[i] += faces[sub*5 + f]
        i += 1
