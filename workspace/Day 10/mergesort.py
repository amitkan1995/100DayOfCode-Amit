# Implement merge sort and its running time

import random
import timeit
arr = []
for x in range(500000):
    arr.append(random.randint(1,500000))

# To check the running time
start = timeit.default_timer()

# Merge Sort's Function:
def merge(left, right, Array):
  i = 0
  j = 0
  k = 0
 
  while (i<len(left) and j<len(right)):
    if(left[i]<right[j]):
      Array[k] = left[i]
      i = i+1
    else:
      Array[k] = right[j]
      j = j+1
 
    k = k+1
  
  while(i<len(left)):
    Array[k] = left[i]
    i = i+1
    k = k+1
  
  while(j<len(right)):
    Array[k] = right[j]
    j = j+1
    k = k+1
 
#function for dividing and calling merge function
def mergesort(Array):
  n = len(Array)
  if(n<2):
    return
 
  mid = int(n/2)
  left = []
  right = []
  
  for i in range(mid):
    number = Array[i]
    left.append(number)  
   
  for i in range(mid,n):
    number = Array[i]
    right.append(number)
 
  mergesort(left)
  mergesort(right)
 
  merge(left,right,Array)
 

mergesort(arr)

stop = timeit.default_timer()
print("Running Time is:")
print (stop - start)
# for i in arr:
#   print (i)