# Sock Merchant Hackerrank

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = set(ar) #1
    socks = {} #2
    pairs = 0 #3
    print(colors)
    for color in colors: #4
        socks[color] = ar.count(color)   
    
    for sock in socks: #6
        pairs += socks[sock] // 2
    return pairs #7

n=9
ar=[10,20,20,10,30,50,10,20]

sockMerchant(n,ar)
