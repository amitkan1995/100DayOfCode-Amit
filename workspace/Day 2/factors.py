#To find factors of the input number

num=int(input("Enter number:"))

factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
    if i>num:
        break

print(factors)