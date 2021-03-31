N = int(input())
W = list(map(int,input().split()))
cnt=0
min_val=10000000
for i in range(len(W)):
  if min_val > abs(sum(W[:i])-sum(W[i:])):
    min_val = abs(sum(W[:i])-sum(W[i:]))
print(min_val)