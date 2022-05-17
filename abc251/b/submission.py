from itertools import *
n, w = map(int, input().split())
a = list(map(int, input().split()))
s = set()
for i in range(1, 4):
    for j in combinations(a, i):
        s.add(sum(j))
ans = sum(i<=w for i in s)
print(ans)
