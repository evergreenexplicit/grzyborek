import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import math
x = np.linspace(-math.pi/2, math.pi/2, 100)
#funkcja + szum
y =np.random.normal(1.6 * np.sin(x)+ 0.5,0.001)
xn = np.linspace(-math.pi/2, math.pi/2, 200)

# funkcja liniowa
a = np.vstack([x, np.ones(len(x))]).T
a,b = np.dot(np.linalg.inv(np.dot(a.T, a)), np.dot(a.T, y))
yn = np.polyval([a,b], xn)

print("Funkcja liniowa, wspolczynniki: ",a,b)
plt.plot(x, y, 'or')
plt.plot(xn, yn)
plt.show()


# funkcja kwadratowa
a,b,c= np.polyfit(x, y, 2)
yn = np.polyval([a,b,c], xn)

print("Funkcja kwadratowa, wspolczynniki: ",a,b,c)
plt.plot(x, y, 'or')
plt.plot(xn, yn)
plt.show()



# a*x^3 + b*x + c
def f_1(x, a, b, c):
    return a*x**3 + b*x + c

def residual_1(p, x, y):
    return y - f_1(x, *p)

p0 = [1., 1., 1.]
popt, pcov = optimize.leastsq(residual_1, p0, args=(x, y))
yn = f_1(xn, *popt)

print("a*x^3 + b*x + c, wspolczynniki: ",popt)
plt.plot(x, y, 'or')
plt.plot(xn, yn)
plt.show()



# a*sin(x)
def f_2(x, a):
    return a* np.sin(x)

def residual_2(p, x, y):
    return y - f_2(x, *p)

p0 = [1.]
popt, pcov = optimize.leastsq(residual_2, p0, args=(x, y))
yn = f_2(xn, *popt)

print("a*sin(x), wspolczynniki: ",popt)
plt.plot(x, y, 'or')
plt.plot(xn, yn)
plt.show()

# a*sin(x) + b
def f_3(x, a,b):
    return a* np.sin(x) + b

def residual_3(p, x, y):
    return y - f_3(x, *p)

p0 = [1.,1.]
popt, pcov = optimize.leastsq(residual_3, p0, args=(x, y))
yn = f_3(xn, *popt)

print("a*sin(x), wspolczynniki: ",popt)
plt.plot(x, y, 'or')
plt.plot(xn, yn)
plt.show()

