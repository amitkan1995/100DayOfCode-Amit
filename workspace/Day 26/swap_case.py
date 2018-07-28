# Swap Case problem from python

#One line simplest solution... print(input().swapcase()) ......  I love the beauty of it.

#Code written on Hackerrank Editor

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)