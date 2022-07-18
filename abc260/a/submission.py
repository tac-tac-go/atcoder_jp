a,b,c = list(input())
if a==b and b==c:
  print(-1)
else:
  if a==b:
    print(c)
  elif b==c:
    print(a)
  else:
    print(b)

