import numpy as np
import matplotlib.pyplot as plt

N = 16 
frequency = 8000
multiplier = frequency/N
n = np.arange(2*N)

y = np.sin(2 * np.pi * n/N) 

plt.stem(n,y)
xs = 500 * n
plt.xticks(n,xs)
plt.show()