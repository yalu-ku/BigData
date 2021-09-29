import matplotlib.pyplot as plt
import random

fre=[]
prob=[]

cnt=0
total_try=30 # 큰 수의 법칙...
before = False

for j in range(1, total_try+1):
    i=random.randint(1,6)
    if i==3:
        if before:
            cnt+=1
        else:
            before=True
    else:
        before = False

        
    #print(i)
#print('cnt:',cnt)

    
    fre.append(cnt/j)
    prob.append(1/6)

plt.plot(range(1, total_try+1), fre, 'b', range(1, total_try+1), prob, 'r')
plt.legend(['Relative Frequency', 'Probability'])
plt.show()
