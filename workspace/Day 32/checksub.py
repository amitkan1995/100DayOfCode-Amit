# Check Subset from Hackerrank

for _ in range(int(input())):
    a = input()
    A = input().split()
    b = input()
    B = input().split()
    print(set(A).intersection(set(B)) == set(A))
    