#import numpy as np
import math
import os

# Read Files
path = os.path.abspath(os.getcwd())
fGenFile = open(path + '\\Project 1\\finger_genuine.score', 'r')
fGen = []
for line in fGenFile.readlines():
    fGen.append(float(line))

fImpFile = open(path + '\\Project 1\\finger_impostor.score', 'r')
fImp = []
for line in fImpFile.readlines():
    fImp.append(float(line))

hGenFile = open(path + '\\Project 1\\hand_genuine.score', 'r')
hGen = []
for line in hGenFile.readlines():
    hGen.append(float(line))

hImpFile = open(path + '\\Project 1\\hand_imposter.score', 'r')
hImp = []
for line in hImpFile.readlines():
    hImp.append(float(line))

print(fGen)




# Close Files
fGenFile.close()
fImpFile.close()
hGenFile.close()
hImpFile.close()