import numpy as np
import matplotlib.pyplot as plt

# Setup 100 linearly spaced scores
s = np.linspace(0, 1, 100)

# PDF of genuine scores
p_genuine = 3*(s**2)

# PDF of imposter scores
p_imposter = 2 - 2*s

# Setting axes
fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(111)
ax1.set_ylabel('P(s)')
ax1.set_xlabel('scores')
ax1.set_title('Score Distribution Curve')

# Plot the functions
plt.plot(s, p_genuine, 'r')
plt.plot(s, p_imposter, 'b')

# Show the plot
plt.show()
