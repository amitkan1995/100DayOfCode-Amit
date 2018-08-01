# Iteratools permutations

from itertools import permutations

str,n=input().split()

# Pythonic solution
print(*[''.join(i) for i in permutations(sorted(str),int(n))],sep='\n')