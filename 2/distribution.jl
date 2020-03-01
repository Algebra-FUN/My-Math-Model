"""
distribution.jl
用于公平指标分配问题的模拟脚本
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
"""

# 总席位数
s = 20
# 各方人数情况
ps = [42,45,33,12,35,80,67,34]
# 初始化席位分配
ns = [0 for _ in ps]
# 定义Q函数
Q(p,n) = p/(n+.5)

println("下面将$(s)个席位分配给$(length(ps))个方面")
println("各方人数情况:$(ps)")
println("-----------------------------------------------")

for r ∈ 1:s
    println("现在进行第$(r)个席位的分配")
    qs = [Q(p,n) for (p,n) in zip(ps,ns)]
    println("Q值：$(qs)")
    i = argmax(qs)
    println("第$(i)方的Q值最大，将席位分给第$(i)方")
    ns[i] += 1
    println("目前各方的席位情况：$(ns)")
    println("-----------------------------------------------")
end