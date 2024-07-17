import numpy as np
import matplotlib.pyplot as plt

# Input control points
P = np.array([[10, 10], [50, 15], [75, 60], [90, 100], [105, 140], 
              [150, 200], [180, 140], [190, 120], [160, 100], [130, 80]])

# Compute Bezier curve using De Casteljau's algorithm
t = np.linspace(0, 1, 100)
Q = P.copy()
for k in range(1, P.shape[0]):
    Q[:P.shape[0]-k, :] = (1-t)*Q[:P.shape[0]-k, :] + t*Q[1:P.shape[0]-k+1, :]
B = Q[0, :]

# Plot original points and Bezier curve
plt.plot(P[:, 0], P[:, 1], 'ro--', label='Control points')
plt.plot(B[0], B[1], 'bo', label='Bezier curve')
plt.legend()
plt.show()
#Visual Studio test