# To check if input string is strong pass word or not.
# 
#   -> Its length is at least 6.
#   -> It contains at least one digit.
#   -> It contains at least one lowercase English character.
#   -> It contains at least one uppercase English character.
#   -> It contains at least one special character. The special characters are: !@#$%^&*()-+


def minimumNumber(n, password):
    count=0
    #To Check for each case
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1    
    # Return the minimum number of characters to make the password strong
    return max(count,6-n)

n=int(input())
password=input()
ans=minimumNumber(n,password)

print("Characters require to make it string password are",format(ans))