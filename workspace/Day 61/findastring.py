# Find a string on Hackerrank
def count_substring(string, sub_string):
    sublen=len(sub_string)
    #print(sublen,":",len(string))
    count=0
    for i in range(0,len(string)):
        if(len(string)-i<sublen):
            break  
        t=string[i:sublen+i]
        if(sub_string==t):
            count=count+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)