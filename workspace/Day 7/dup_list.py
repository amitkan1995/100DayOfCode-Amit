# To print duplicate element in the list

li=[1,6,2,5,1,4,2,5]

dup=set([x for x in li if li.count(x)>1])
print(dup)