N,K=list(map(int, input().split()))
Sl=[input() for _ in range(N)]
for s in sorted(Sl[:K]):
  print(s)
