n, d = map(int, input().split())
l = sorted(map(int, input().split()), reverse=True)
ans = 0
m = n//d
for i in range(m):
    ans += min(l[d*i:d*(i+1)])
print(ans)
