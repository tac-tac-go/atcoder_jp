from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
B = [0] + list(accumulate(A))
for k in range(n):
    print(max([B[i + k + 1] - B[i] for i in range(n - k)]))
