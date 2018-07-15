# To convert A decimal number can be negative or postive to Binary


def decimalToBinary(n):
    b1=bin(n) 
    return (b1[2:])

def negBin(n):
    n=~n
    print(n)
    b=bin(n)
    #b=b[2:]
    temp=bin(1)
    #temp=temp[2:]
    #print(temp)
    print(int(b,2))
    b2=bin(b)+bin(temp)
    #b2=bin(int(b,2)+int(temp,2))
    b2=b2[2:]
    #print (~b2)
    print (b2)
    

    




n=int(input())

b=decimalToBinary(n) if n>=0 else negBin(n)
print(b)