# Selection Sort with running time complexity

import random
import timeit
A = []
for x in range(1000):
    A.append(random.randint(1,1000))

# To check the running time
start = timeit.default_timer()

for i in range(len(A)):
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
             
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]

stop = timeit.default_timer()
print("Running Time in O(n^2)")
print (stop - start)