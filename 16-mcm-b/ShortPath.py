inf = float('inf')

# w:邻接矩阵,u0:初始点
def dijkstra(w, u0):
    # n:图中点个数
    n = len(w)
    # d:u0->i点距离
    d = [w[u0][v] if v is not u0 else 0 for v in range(n)]
    # p:u0->i路程途径点
    p = [u0 if w[u0][i] < inf else -1 for i in range(n)]
    # U:全部点组成的集合
    U = set(range(n))
    # S:已确定最短距离的点集
    S = {u0}
    # 重复n-1次
    for _ in range(n-1):
        # 当前达到最短距离的点
        u = min(U - S, key=lambda x: d[x])
        # 将u加入S
        S |= {u}
        for v in U - S:
            if d[u] + w[u][v] < d[v]:
                d[v] = d[u] + w[u][v]
                p[v] = u
    return d, p


def trace_back(p, u0):
    n = len(p)
    paths = [[v] for v in range(n)]
    for v, path in enumerate(paths):
        while v not in (u0,-1):
            v = p[v]
            path.append(v)
    return [tuple(_[::-1]) for _ in paths]


def Dijkstra(w, u0):
    d, p = dijkstra(w, u0)
    return d, trace_back(p, u0)


def floyd(A):
    n = len(A)
    P = [[i if A[i][j] < inf else -1 for j in range(n)] for i in range(n)]
    for k in range(n):
        P = [[k if A[i][k]+A[k][j] < A[i][j] else p for j,
              p in enumerate(r)] for i, r in enumerate(P)]
        A = [[min(A[i][j], A[i][k]+A[k][j]) for j in range(n)]
             for i in range(n)]
    return A, P


def Floyd(A):
    A, P = floyd(A)
    return A, [*map(trace_back, P, range(len(A)))]


if __name__ == "__main__":
    A = [
        [0, 50, inf, 40, 25, 10],
        [50, 0, 15, 20, inf, 25],
        [inf, 15, 0, 10, 20, inf],
        [40, 20, 10, 0, 10, 25],
        [25, inf, 20, 10, 0, 55],
        [10, 25, inf, 25, 55, 0]
    ]
    # for i in range(6):
    #     print(Dijkstra(A, i))
    dis,path = Floyd(A)
    print(path)
