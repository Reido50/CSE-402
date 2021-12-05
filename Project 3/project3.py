import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
from scipy import signal
import scipy
import math
import os
import sys
import csv
import copy

def ShowBrightenImage(img, value):
    brightened = ImageEnhance.Brightness(img).enhance(value)
    brightened.show()

def ShowContrastedImage(img, value):
    contrasted = ImageEnhance.Contrast(img).enhance(value)
    contrasted.show()

# Question 1
# (a)
filename = 'face_grey.jpg'
path = os.path.abspath(os.getcwd())
img = Image.open(path + '\\Project 3\\' + filename)
img_mat = np.array(img)
ShowBrightenImage(img, 1.5)
ShowContrastedImage(img, 1.5)
