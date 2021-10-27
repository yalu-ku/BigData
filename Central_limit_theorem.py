# CLT : Central limit theorem
import random

total = 10
n = 5
rand_v = []
for i in range(total):
    s = 0
    for j in range(n):
        r_int = random.randint(1,5)
        print('random int:', r_int, end="")
        s += r_int
        print('\ts:',s,'\tj:',j)
    rand_v.append(s)
    print('rand_v:',rand_v)
    
print(rand_v)
