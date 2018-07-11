# To implemet bubble sort
import random
import timeit
arr = []
for x in range(1000):
    arr.append(random.randint(1,1000))

# To check the running time
start = timeit.default_timer()

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above

bubbleSort(arr)

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("%d" %arr[i]), 


stop = timeit.default_timer()
print("Running Time in O(n^2)")
print (stop - start)