import random

total = 1000
rand_v = [random.randint(1,5) for _ in range(total)]

def mean(X):
    return sum(X)/len(X)

def variance(rand_v):
    s = 0
    for i in range(len(rand_v)):
        s += (rand_v[i] - mean(rand_v))**2
    return s/len(rand_v)

print(mean(rand_v))
print(variance(rand_v))
