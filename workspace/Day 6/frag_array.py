# In an array to shift all 0 to right most end.
# And Maintaining the relative order of elements

def pushZeroes(arr):
    c=0
    # First move all non zero to one end
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[c]=arr[i]
            c+=1
    # Then move 0's to other end
    while c<len(arr):
        arr[c]=0
        c+=1
    print(arr)

ar=[10,12,0,0,7,19,7,0,45,5]
pushZeroes(ar)