from collections import Counter
N = int(input())
A = list(map(int,input().split()))
print(Counter([i for i in range(2,max(A)+1) for j in A if j%i==0]).most_common()[0][0])