import numpy as np #결과값이 맞는지 확인하기 위해 사용, 코드에서는 사용하지 않았습니다. 

X = [1,2,3,4,5]
Y = [2,4,3,1,1]

def mean(x):
    return sum(x)/len(x)

def sqrt(x):
    return x **.5

def variance(x):
    tmp = []
    for i in x:
        tmp.append((i-mean(x))**2) #편차제곱
    return sum(tmp)/len(x)

def std(x):
    return sqrt(variance(x))

def corr(x, y):
    s = 0
    for i in range(len(x)):
        s += x[i] * y[i]
    return s/len(x)

def exp(x):
    s = 0
    for i in x:
        s += i / len(x)
    return s

covariance = corr(X,Y) - (exp(X)*exp(Y))
corr_coef = covariance/(std(X)*std(Y))


print(corr_coef)
print(np.corrcoef(X,Y)) # 확인용 코드

# print(mean(X))
# print(exp(X))

# print(np.e)
# print(std(X))
# print(np.std(X))

# print(variance(X))
# print(np.var(X))

# print(mean(X))
