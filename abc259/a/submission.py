n,m,x,t,d = map(int,input().split())

if m>=x:
  print(t)
else:
  result = t-(x-m)*d
  print(result)
