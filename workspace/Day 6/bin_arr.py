# To sort Binary Array in linear time

def bin_arr(ar):
    j=-1
    for i in range(len(ar)):
        if ar[i]<1:
            j+=1
            print(ar)
            ar[j],ar[i]=ar[i],ar[j]
    #print(ar)

#Its working is exactly like quick sort
# But in linear time
arr=[1,0,1,1,0,1,0]

bin_arr(arr)
