N = int(input())
S = list(map(int, input().split()))
ans = 0
for s in S:
  flag = False
  for a in range(1, 333):
    for b in range(1, 333):
      if 4*a*b+3*a+3*b == s:
        flag = True
  if not flag:
    ans += 1

print(ans)
