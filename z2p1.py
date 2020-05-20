import numpy as np
import matplotlib.pyplot as plt

#Suma dwóch sinusoid sin(x) + sin(2*x)

x = np.linspace(0, 6.5*np.pi, 200)
y1 = np.sin(x)
y2 = np.sin(2*x)

y = y1+y2

plt.plot(x, y, color='r', lw=2)

plt.text(0,0,"Suma dwóch sinusoid sin(x) + sin(2*x)")
plt.show()



#Sygnał sinusoidalny modulowany amplitudowo sygnałem sinusoidalnym


sampling_frequency = 40000
freq = 10 #Hz

x = np.arange(0,1,1.0/sampling_frequency)
y = np.sin(2 * np.pi * freq * x + (np.pi/2)) * np.sin(np.pi * x + (np.pi/2))

plt.text(0,0,"Sygnał sinusoidalny modulowany amplitudowo sygnałem sinusoidalnym")
plt.plot(x,y)
plt.show()

#Sygnał próbkowany nierównomiernie


freq = 10 #Hz
#x^3 dla 10 < x 11
x = np.array([x**3 for x in np.arange(10,11,1.0/200)])
print(x)
def uneven(x):
    return np.sin(2 * np.pi * freq * x + (np.pi/2))

y = uneven(x)



plt.text(0,0,"Sygnał próbkowany nierównomiernie")
plt.plot(x,y)

plt.show()