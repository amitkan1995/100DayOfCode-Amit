#Hackerrank set intro problem.

def average(array):
    # your code goes here
    heights = set(array)
    averg = sum(heights) / len(heights)
    return averg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)