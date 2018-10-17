# Python program to check if there is Pythagorean 
# triplet in given array 
  
# Returns true if there is Pythagorean 
# triplet in ar[0..n-1] 
  
def isTriplet(ar, n): 
    j=0
      
    for i in range(n - 2): 
        for k in range(j + 1, n): 
            for j in range(i + 1, n - 1): 
                # Calculate square of array elements 
                x = ar[i]*ar[i] 
                y = ar[j]*ar[j] 
                z = ar[k]*ar[k]  
                if (x == y + z or y == x + z or z == x + y): 
                    return 1
      
    # If we reach here, no triplet found 
    return 0
  
  
# Driver program to test above function  
ar = [3, 1, 4, 6, 5] 
ar_size = len(ar) 
  
if(isTriplet(ar, ar_size)): 
    print("Yes") 
else: 
    print("No") 
  