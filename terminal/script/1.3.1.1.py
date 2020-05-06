import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt  

I = np.array([0,0,.05,.05,.1,.1,.2,1,1])
r = 50
beta = [1,.6,.7,.7,.7,.8,.9,.9]
KM = 500
init = [100*(.7**i) for i in range(9)]

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

df = pd.DataFrame(columns=[i for i in range(1,10)])
df.loc[0] = init
for i in range(200):
    P = df.loc[len(df)-1]
    df.loc[len(df)] = L(P) @ P

for i in range(2,10):
    plt.plot([*range(len(df))],df[i],label=i)
plt.legend()
plt.show()