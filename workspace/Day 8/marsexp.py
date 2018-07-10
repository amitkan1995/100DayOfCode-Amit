# Hackerrank Mars Exploration Problem
# Link is https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    ak=0
    for i in range(len(s)):
        k=i%3
        if k==0 and s[i]!='S':
            ak+=1
        if k==1 and s[i]!='O':
            ak+=1
        if k==2 and s[i]!='S':
            ak+=1
    return ak

s = input()
result = marsExploration(s)
print(result)