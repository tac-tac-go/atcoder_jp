n = int(input())
t = [0] * (n+1)
k = [0] * (n+1)
a = [0] * (n+1)

for i in range(1, n+1):
  inp = list(map(int, input().split()))
  t[i] = inp[0]
  k[i] = inp[1]
  a[i] = inp[2:]

need = [False] * (n+1)
need[n] = True

for i in range(n, 0, -1):
  if not need[i]:
    continue
  for child in a[i]:
    need[child] = True
print(sum(t[i] for i in range(1, n+1) if need[i]))
