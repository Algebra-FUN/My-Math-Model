import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt  

I = np.array([0,0,2/30,3/30,5/30,7/30,8/30,1,1])
r = 100
beta = [1,.4,.5,.5,.5,.7,.9,.9]
KM = 500
init = [10*(.5**i) for i in range(9)]
weeks = 200

def K(P):
    return I @ P

def F(k):
    return r*(1-k/KM)

def S(x,k):
    return beta[x]*(1 if x < 3 else (1-k/KM))

def L(P):
    k = K(P)
    A = np.zeros((9,9))
    for i in range(8):
        A[i+1,i] = S(i,k)
    A[0,8] = F(k)
    return A

df = pd.DataFrame(columns=[*range(1,10)])
df.loc[0] = init
for i in range(weeks):
    P = df.loc[len(df)-1]
    df.loc[len(df)] = L(P) @ P

df['egg'] = df[1] + df[2]
df['junior larvae'] = df[3] + df[4] + df[5]
df['senior larvae'] = df[6] + df[7]
df['adult'] = df[8] + df[9]

for age in ['egg','junior larvae','senior larvae','adult']:
    plt.plot([*range(len(df))],df[age]*10**3,label=age)
plt.yscale('log')
plt.title(f'for {weeks} weeks')
plt.xlabel('weeks')
plt.ylabel('amount of locusts')
plt.legend()
plt.show()

print(df.loc[200])