n, k = map(int, input().split())
an = list(map(int, input().split()))
max_val = -1
flag = False
for ai in an:
  if k >= ai:
    if max_val < ai:
      max_val = ai
      flag = True
print(an.index(max_val)+1) if flag else print(-1)
