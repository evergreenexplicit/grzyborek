import numpy as np
import matplotlib.pyplot as plt
import math
X = np.linspace(-math.pi/2, math.pi/2, 100)
Y =np.random.normal(1.6 * np.sin(X)+ 0.5,0.001)
xn = np.linspace(0, 10, 200)

a = np.vstack([X, np.ones(len(X))]).T
m,c = np.dot(np.linalg.inv(np.dot(a.T, a)), np.dot(a.T, Y))
yn = np.polyval([m, c], xn)

plt.plot(X,Y,'or')
plt.plot(xn,yn)
plt.show()

