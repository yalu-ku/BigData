## Simple Regression Analysis

import numpy as np
import matplotlib.pyplot as plt

# Make Data
x = np.linspace(0,4,15)
sigma = 1
error = np.random.normal(0, sigma, len(x))
y = 2 + 3*x + error


def cov(x_, y_):
    s=0
    for i in range(len(x_)):
        s += x_[i]*y_[i]
    return (s/len(x_))-(mean(x_)*mean(y_))   # E[XY] - E[X]E[Y]

def mean(x_):
    s=0
    for i in x_:
        s += i
    return s/len(x_)

def var(x_):
    s=0
    m=mean(x_)
    for i in x_:
        s += (i-m)**2   # Xi 값의 평균과 차이
    return s/(len(x_)-1)


# Main
a = cov(x,y)/var(x)
b = mean(y) - 3*mean(x)     #a=3

y_a = 2 + a*x
y_b = b + 3*x

plt.figure(1)
plt.plot(x, y, 'b.', label='real data')
plt.plot(x, y_a, 'r-', label='estimation')
plt.figure(2)
plt.plot(x, y, 'b.', label='real data')
plt.plot(x, y_b, 'r-', label='estimation')
plt.show()

'''
beta1 = cov(x,y)/var(x)
beta11 = np.cov(x,y)[0,1]/np.var(x)

beta0 = mean(y) - beta1*mean(x)
beta00 = np.mean(y) - beta11 * np.mean(x)
print(beta1, beta0)

y_h = beta0 + beta1*x
y_hh = beta00 + beta11*x

##plt.ylim(x, y, (0,4))

plt.plot(x, y, 'b.', label='real data')
plt.plot(x, y_h, 'r-', label='estimation')
plt.legend()
plt.show()
'''
