def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("Select Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")

choice=input("Enter choice (1-4) : ")

#Taking input from user
num1=int(input("Enter 1st number : "))

num2=int(input("Enter 2nd number : "))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':   
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='3':
    print(num1,"X",num2,"=",mul(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("Invalid Input")