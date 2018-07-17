# To count the frequency of alphabet in a string

def count(st):
    occur={}
    for i in st:
        kys=occur.keys()
        if i in kys:
            occur[i]+=1
        else:
            occur[i]=1
    return occur


print(count('Biscuits.com'))
