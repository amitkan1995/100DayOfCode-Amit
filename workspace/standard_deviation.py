# 10 Days of Statistics standard deviation problem


n=int(input())
l=[int(x) for x in input().split()]
dev=sum(l)/len(l)
su=0
for i in range(len(l)):
    sdl=l[i]-int(dev)
    su=su+((sdl**2))
print(round(float((su/len(l))**0.5),1))