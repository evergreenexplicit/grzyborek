import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

x =  np.arange(1,10,10.0/44100)
y1 = np.sin(x)
y2 = signal.square(x)
y3 = signal.sawtooth(x)
y4 = signal.gausspulse(x)
plt.subplot(2, 2, 1)
plt.plot(x, y1)

plt.subplot(2, 2, 2)
plt.plot(x, y2)

plt.subplot(2, 2, 3)
plt.plot(x, y3)

plt.subplot(2, 2, 4)
plt.plot(x, y4)

plt.show()

#Wyprostowany jednopołówkowo
y = np.sin(x)
y5 = y.clip(min=0)

plt.subplot(2, 1, 1)
plt.plot(x, y5)

#Wyprostowany dwupołowkowo
y6 = np.absolute(y)

plt.subplot(2, 1, 2)
plt.plot(x, y6)

plt.show()





#suma składowej stałej i  harmonicznych:
ys = []
frequency = 1 #Hz
for i in np.arange(1,20):
    ys.append( (1.0/(i)) * np.sin(2 * np.pi * x *  i * frequency) )

output = np.array(ys)
output = output.sum(axis=0)
plt.plot(x,output)
plt.show()