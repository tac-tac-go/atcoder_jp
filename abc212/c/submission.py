from bisect import bisect_right
INF = 10**11
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))+[-INF, INF]
a.sort()
b.sort()
ans = 10**10
for x in a:
  pos = bisect_right(b, x)
  ans = min(ans, abs(b[pos]-x))
  ans = min(ans, abs(b[pos-1]-x))
print(ans)
