n = int(input())
an = list(map(int, input().split()))
ans = -9999
for i in range(n):
  mi = an[i]
  ans = max(an[i], ans)
  for j in range(i, n):
    mi = min(mi, an[j])
    ans = max(ans, mi*(j-i+1))
print(ans)
