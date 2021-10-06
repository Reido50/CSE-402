import numpy as np
import matplotlib.pyplot as plt

# Setup 100 linearly spaced scores
s = np.linspace(0, 1, 100)

# Calculate FMR values
FMR = []
FNMR = []
for i in s:
    FMR.append((2.0-1.0)-(2.0*i - i**2.0))
    FNMR.append(i**3.0)


# Setting axes
fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(111)
ax1.set_ylabel('FNMR')
ax1.set_xlabel('FMR')
ax1.set_title('DET Curve')

# Plot the functions
plt.plot(FMR, FNMR, 'r')

# Show the plot
plt.show()
