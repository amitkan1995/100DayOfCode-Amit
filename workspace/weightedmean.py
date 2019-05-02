# Hackerrank 10 Days of Statistics Problem

# Weighted Mean

N = map(int,input().split())
#print (N)
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))