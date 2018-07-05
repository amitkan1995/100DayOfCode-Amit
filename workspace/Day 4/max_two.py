# To find two largest number in array in minimum complexity
# It is done in O(n) 
def max(lst):
    ma=lst[0]
    
    for i in lst:
        if i>ma:
            ma=i
    
    return ma           


lst=[10,55,1,45,23,56,6,8,4]
#First Find the maximum
m=max(lst)
c_list=lst[:]

#Then remove maximum from duplicate list
c_list.remove(m)
m2=max(c_list)
print("Maximum is {} and Second Maximum is {}".format(m,m2))