t, a, b, c, d = map(int, input().split())
if a+c <= t:
  print(b+d)
elif c+a > t and c<=t:
  print(d)
elif c+a > t and a<=t:
  print(b)
else:
  print(0)
