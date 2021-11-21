s, t, x = map(int, input().split())
seach = []
if s < t:
  search = list(range(s, t))
else:
  search = list(range(24, s-1, -1))+list(range(1, t,1))
if x in search:
  print("Yes")
else:
  print("No")
