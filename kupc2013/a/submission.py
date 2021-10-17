N, Q = map(int, input().split())
yn = []
ans = "kogakubu10gokan"
for i in range(N):
  y, n = input().split()
  if int(y) <= Q:
    ans = n
print(ans)
