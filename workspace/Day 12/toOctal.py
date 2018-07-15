# To convert +ve Decimal number to its Octal Representation

def decimalToBinary(n):
 
    if n > 1:
         #  divide with integral result 
         # (discard remainder) 
        decimalToBinary(n//8) 
 
    print(n%8,end ='')      


n=int(input())
decimalToBinary(n)