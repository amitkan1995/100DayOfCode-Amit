# Set Mutation problem from hackerrank


a = int(input())
s = set(int(x) for x in input().split())
n = int(input())

for i in range(n):
    cmd = input().split()
    if cmd[0] == "update":
        u = set(int(x) for x in input().split())
        s.update(u)
    elif cmd[0] == "intersection_update":
        iu = set(int(x) for x in input().split())
        s.intersection_update(iu)
    elif cmd[0] == "difference_update":
        du = set(int(x) for x in input().split())
        s.difference_update(du)
    else:
        sdf = set(int(x) for x in input().split())
        s.symmetric_difference_update(sdf)

print(sum(s))