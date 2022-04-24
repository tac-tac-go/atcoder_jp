def solve():
  a, b, c, d, e, f, x = map(int,input().split())
  aoki = 0
  takahashi = 0
  for t in range(x):
    if t%(a+c) < a:
      takahashi += b
    if t%(d+f) < d:
      aoki += e
  if aoki == takahashi:
    return "Draw"
  elif aoki > takahashi:
    return "Aoki"
  else:
    return "Takahashi"
print(solve())
