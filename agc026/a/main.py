from itertools import groupby
n = int(input())
a = list(map(int,input().split()))
ans =0
for (key,group) in groupby(a):
  ans += len(list(group))//2
print(ans)