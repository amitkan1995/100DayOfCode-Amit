# Hackerrank tuple problem 

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list) # We need to create a tuple as lists are not hashable
    print(hash(t)) # Print the hash value of the tuple
