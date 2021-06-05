a,b,t = map(int,input().split())
start = a
while start<t:
  start+=b-a
print(start)