# Symmetric Difference in hackerrank

M = input()
m = set(list(map(int,input().split())))
print(m)
N = input()
n = set(list(map(int,input().split())))

a = list(m.difference(n))
b = list(n.difference(m))

a.extend(b)

[print(i) for i in sorted(a)]