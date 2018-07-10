# Hackerrank "HackerRank in a String!"Problem 
# Link is https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def hackerrankInString(s):
    st='hackerrank'
    s=list(s)
    #If String input string is shorter then it is not possible.
    if len(st)> len(s):
        return 'NO'
    for i in st:
        if i not in s:
            return 'NO'
        else:
            #print(s.index(i)+1)
            s=s[s.index(i)+1:]
    return 'YES'

q = int(input())

for q_itr in range(q):
    s = input()
    result = hackerrankInString(s)
    print(result,"\n")

