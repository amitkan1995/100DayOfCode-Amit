# To find the minimum missing value from a sorted list

def minMissing(arr):
    for i in range(len(arr)):
        if (i!=arr[i]):
            return i

    



arr=[0, 1, 3, 4, 5, 7, 10]
ms=minMissing(arr)
print ("Missing Number is: {}".format(ms))