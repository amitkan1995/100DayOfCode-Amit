# To print a staircase in reverse way

#If input is 5

#output will be.

#       *
#      **
#     ***
#    ****
#   *****

def staircase(n):
    print('\n'.join([' '*(n-i) + '*'*i for i in range(1,n+1)]))
    #One line solution to it

n=int(input("Enter input number"))

staircase(n)
