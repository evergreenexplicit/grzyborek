import numpy as np


a = "-2 2 2 2; 2 -2 2 2; 2 2 -2 2; 2 2 2 -2"
A = np.matrix(a)
b = "32; 12; 12; 32"
B = np.matrix(b)
result = np.linalg.inv(A).dot(B)
print(result)
