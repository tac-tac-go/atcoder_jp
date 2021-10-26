import itertools
N, Q = map(int, input().split())
S = input()
AC = [0] * (N)
for i in range(1, N):
  if S[i-1] == 'A' and S[i] == 'C':
    AC[i] = 1
SAC = [0] + list(itertools.accumulate(AC))
for i in range(Q):
  l, r = map(int, input().split())
  print(SAC[r]-SAC[l])
