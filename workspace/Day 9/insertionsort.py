# Implementing Insertion Sort

import random
import timeit
arr = []
for x in range(10000):
    arr.append(random.randint(1,10000))

# To check the running time
start = timeit.default_timer()

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

insertionSort(arr)

stop = timeit.default_timer()
print("Running Time in O(n^2)")
print (stop - start)