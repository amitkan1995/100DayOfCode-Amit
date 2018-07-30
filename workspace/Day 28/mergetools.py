# Merge the tools problem

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        ls=[]
        for j in range(i,i+k):
            if string[j] not in ls:
                  ls.append(string[j])
        print(''.join(ls))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)