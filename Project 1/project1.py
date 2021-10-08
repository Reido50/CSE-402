import numpy as np
import matplotlib.pyplot as plt
import math
import os

def thresholdAnalyser(gen:np.array, imp:np.array, eta):
    FMR = 0
    FNMR = 0
    # Calculate FMR
    for score in imp:
        if score > eta:
            FMR += 1
    FMR /= float(len(imp))
    #Calculate FNMR
    for score in gen:
        if score < eta:
            FNMR += 1
    FNMR /= float(len(gen))
    # Return as a tuple
    return (FMR, FNMR)

def plotDET(gen:np.array, imp:np.array, dist:bool):
    # Setup 100 linearly spaced thresholds
    t = np.linspace(0, 966, 1000)
    FMRs = []
    FNMRs = []
    for eta in t:
        if dist:
            FNMR, FMR = thresholdAnalyser(imp, gen, eta)
        else:
            FMR, FNMR = thresholdAnalyser(gen, imp, eta)
        FMRs.append(FMR)
        FNMRs.append(FNMR)
    # Setting axes
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('FNMR')
    ax1.set_xlabel('FMR')
    ax1.set_title('DET Curve')
    # Plot the functions
    plt.plot(FMRs, FNMRs, 'r')
    # Show the plot
    plt.show()


# Read Files
path = os.path.abspath(os.getcwd())
# Finger Genuine Scores
fGenFile = open(path + '\\Project 1\\finger_genuine.score', 'r')
fGen = []
for line in fGenFile.readlines():
    fGen.append(float(line))
fGen = np.array(fGen)
# Finger Impostor Scores
fImpFile = open(path + '\\Project 1\\finger_impostor.score', 'r')
fImp = []
for line in fImpFile.readlines():
    fImp.append(float(line))
fImp = np.array(fImp)
# Hand Genuine Scores
hGenFile = open(path + '\\Project 1\\hand_genuine.score', 'r')
hGen = []
for line in hGenFile.readlines():
    hGen.append(float(line))
hGen = np.array(hGen)
# Hand Impostor Scores
hImpFile = open(path + '\\Project 1\\hand_impostor.score', 'r')
hImp = []
for line in hImpFile.readlines():
    hImp.append(float(line))
hImp = np.array(hImp)

# (a)
# Finger Score Counts
print("The fingerprint matcher has " + str(len(fGen)) + " genuine scores and " + str(len(fImp)) + " impostor scores.")
# Hand Score Counts
print("The hand matcher has " + str(len(hGen)) + " genuine scores and " + str(len(hImp)) + " impostor scores.\n")

# (b)
# Finger Genuine Max/Min
print("The fingerprint genuine scores maximum value is " + str(max(fGen)) + " while the minimum value is " + str(min(fGen)))
# Finger Impostor Max/Min
print("The fingerprint impostor scores maximum value is " + str(max(fImp)) + " while the minimum value is " + str(min(fImp)))
# Hand Genuine Max/Min
print("The hand genuine scores maximum value is " + str(max(hGen)) + " while the minimum value is " + str(min(hGen)))
# Hand Impostor Max/Min
print("The hand impostor scores maximum value is " + str(max(hImp)) + " while the minimum value is " + str(min(hImp)) + "\n")

# (c)
# Finger Genuine mean and stddev
print("The mean of fingerprint genuine scores is " + str(np.mean(fGen)) + " and the standard deviation is " + str(np.std(fGen)))
# Finger Impostor mean and stddev
print("The mean of fingerprint impostor scores is " + str(np.mean(fImp)) + " and the standard deviation is " + str(np.std(fImp)))
# Hand Genuine mean and stddev
print("The mean of hand genuine scores is " + str(np.mean(hGen)) + " and the standard deviation is " + str(np.std(hGen)))
# Hand Impostor mean and stddev
print("The mean of hand impostor scores is " + str(np.mean(hImp)) + " and the standard deviation is " + str(np.std(hImp)) + "\n")

# (d)
# Finger d-prime
print("The d-prime value for the fingerprint matcher is " + str(math.sqrt(2) * abs(np.mean(fGen) - np.mean(fImp)/math.sqrt(np.std(fGen)**2 + np.std(fImp)**2))))
# Hand d-prime
print("The d-prime value for the hand matcher is " + str(math.sqrt(2) * abs(np.mean(hGen) - np.mean(hImp)/math.sqrt(np.std(hGen)**2 + np.std(hImp)**2))) + "\n")

# (e)
# Finger histogram
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_ylabel('P(s)')
ax1.set_xlabel('scores')
ax1.set_title('Fingerprint Score Histogram')
bins = 10
plt.hist(fGen, bins, alpha=0.75, color="b", label="Genuine")
plt.hist(fImp, bins, alpha=0.75, color="r", label="Impostor")
plt.legend(loc="upper right")
plt.show()
# Hand histogram
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_ylabel('P(s)')
ax1.set_xlabel('scores')
ax1.set_title('Hand Score Histogram')
bins = 10
plt.hist(hGen, bins, alpha=0.75, color="b", label="Genuine")
plt.hist(hImp, bins, alpha=0.75, color="r", label="Impostor")
plt.legend(loc="upper right")
plt.show()

# (f)
eta = 45
# Fingerprint FMR and FNMR
fFMR, fFNMR = thresholdAnalyser(fGen, fImp, eta)
print("The FMR of the fingerprint matcher is " + str(fFMR) + " and the FNMR is " + str(fFNMR))
# Hand FMR and FNMR
hFNMR, hFMR = thresholdAnalyser(hImp, hGen, eta)
print("The FMR of the hand matcher is " + str(hFMR) + " and the FNMR is " + str(hFNMR))

# (g)
# Fingerprint DET Curve
plotDET(fGen, fImp, False)
# Hand DET Curve
plotDET(hGen, hImp, True)



# Close Files
fGenFile.close()
fImpFile.close()
hGenFile.close()
hImpFile.close()
