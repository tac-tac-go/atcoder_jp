s = input()[::-1]
try:
  print(len(s)-s.index("a"))
except:
  print(-1)
