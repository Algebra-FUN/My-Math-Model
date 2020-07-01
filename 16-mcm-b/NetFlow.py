from .ShortPath import Floyd
import numpy as np

m = 5

# 参数
odm = np.matrix()
T0 = np.matrix()
C = np.matrix()
alpha,beta = 1,4

# 初始化
T = np.copy(T0)
Q = np.zeros(T0)

def updateT():
    T = T0*(1+alpha*((Q/C)**beta))

def updateQ(cq,spm):
    for i in range(m):
        for j in range(m):
            path = spm[i,j]
            for k in range(len(path)-1):
                s,t = path[k],path[k+1]
                Q[s,t] += cq[i,j]

# 分组批次    
n = 10

for i in range(n):
    dis,spm = Floyd(T)
    updateQ(Q/n,spm)
    updateT()

print(Q)