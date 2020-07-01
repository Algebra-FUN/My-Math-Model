from ShortPath import Floyd
import numpy as np

inf = float('inf')


def netflow(OD, T0, C, n=30, alpha=1, beta=2):
    m = len(T0)

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

    for i in range(n):
        _, P = Floyd(T)
        updateQ(OD/n, P)
        T = updateT()

    return Q, T


if __name__ == "__main__":
    # 参数设定
    T0 = np.array([
        [inf, 2, 1, inf],
        [inf, inf, inf, 2],
        [inf, inf, inf, 1],
        [inf, inf, inf, inf]
    ])
    OD = np.array([
        [0, 0, 0, 1000],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])
    C = np.array([
        [1, 500, 100, 100],
        [1, 1, 1, 500],
        [1, 1, 1, 100],
        [1, 1, 1, 1]
    ])

    def evalue(T):
        sum,i=0,0
        for v in T.flatten():
            if v < inf:
                sum +=v
                i += 1
        return sum/i

    print('增加道路1-4之前:')
    Q, T = netflow(OD,T0,C)
    print('Q=', Q)
    print('evalue=',evalue(T))

    print('增加道路1-4之后:')
    T0[0,3] = 1.5
    Q, T = netflow(OD,T0,C)
    print('Q=', Q)
    print('evalue=',evalue(T))
