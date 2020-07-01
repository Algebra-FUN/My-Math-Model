from ShortPath import Floyd
import numpy as np

inf = float('inf')

m = 4

# 参数
OD = np.array([
    [0,0,0,1000],
    [0,0,0,0],
    [0,0,0,0],  
    [0,0,0,0]    
])
T0 = np.array([
    [inf,2,1,1.5],
    [inf,inf,inf,2],
    [inf,inf,inf,1],
    [inf,inf,inf,inf]
])
C = np.array([
    [1,500,100,100],
    [1,1,1,500],
    [1,1,1,100],
    [1,1,1,1]
])
alpha, beta = 1, 2

# 初始化
T = np.array(T0)
Q = np.zeros_like(T0)


def updateQ(COD, P):
    P = np.array(P)
    for i in range(m):
        for j in range(m):
            path = P[i, j]
            for k in range(len(path)-1):
                s, t = path[k], path[k+1]
                Q[s, t] += COD[i, j]

def updateT():
    return T0*(1+alpha*((Q/C)**beta))

# 分组批次
n = 20

for i in range(n):
    # print(f'turns {i}/{n}')
    _, P = Floyd(T)
    updateQ(OD/n, P)
    # print(Q)
    T = updateT()
    # print(T)

def evalue():
    value = 0
    i = 0
    for v in T.flatten():
        if v < inf:
            value += v
            i += 1
    return value/i

print(Q)
print(evalue())
