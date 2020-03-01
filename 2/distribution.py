'''
distribution.py
用于公平指标分配问题的模拟脚本
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
'''

from numpy import argmax

# 总席位数
s = 20
# 各方人数情况
ps = [42,45,33,12,35,80,67,34]
# 初始化席位分配
ns = [0 for _ in ps]

# 定义Q函数
def Q(p,n):
    return p/(n+.5)

print('下面将{}个席位分配给{}个方面'.format(s,len(ps)))
print('各方人数情况:',ps)
print('-----------------------------------------------')

for r in range(s):
    print('现在进行第{}个席位的分配'.format(r+1))
    qs = [Q(*x) for x in zip(ps,ns)]
    print('Q值：',qs)
    i = argmax(qs)
    print('第{i}方的Q值最大，将席位分给第{i}方'.format(i=i+1))
    ns[i] += 1
    print('目前各方的席位情况：',ns)
    print('-----------------------------------------------')