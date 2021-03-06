from ShortPath import Floyd
import numpy as np

inf = float('inf')


def netflow(OD, T0, C, n=100, alpha=1, beta=.5):
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

    return Q, T, T/T0 - 1


if __name__ == "__main__":
    # 参数设定
    T0 = np.array([
        [inf, 2, 1, inf],
        [inf, inf, inf, 2],
        [inf, inf, inf, 1],
        [inf, inf, inf, inf]
    ])
    OD = np.array([
        [0, 200, 0, 1000],
        [0, 0, 0, 0],
        [0, 0, 0, 200],
        [0, 0, 0, 0]
    ])
    C = np.array([
        [1, 500, 100, 1],
        [1, 1, 1, 500],
        [1, 1, 1, 100],
        [1, 1, 1, 1]
    ])


    def evalue(Q, T, J):
        RT = T[(T != inf)]
        QT = (Q*T).flatten()
        QT = QT[~np.isnan(QT)]
        J = J.flatten()
        J = J[~np.isnan(J)]
        return {
            '平均道路通行时间': np.mean(RT),
            '加权路网通行时耗': np.sum(QT),
            '路网拥堵指数': np.mean(np.log(J))
        }

    

    print('增加道路1-4之前:')
    Q, T, J = netflow(OD, T0, C)
    print('Q=', Q)
    print('J=', J)
    eval0 = evalue(Q, T, J)
    print('evalue=', eval0)

    print('增加道路1-4之后:')
    T0[0, 3] = 1.5
    C[0, 3] = 75
    Q, T, J = netflow(OD, T0, C)
    print('Q=', Q)
    print('J=', J)
    eval1 = evalue(Q, T, J)
    print('evalue=', eval1)

    def eval_enhance(eval0,eval1):
        for (k, v0), (_, v1) in zip(eval0.items(), eval1.items()):
            print(f'{k} 提高：{(v0-v1)/v0*100}%')
    print('网络提升效果：')
    eval_enhance(eval0,eval1)
