N = int(input())
A = [input().split() for i in range(N)]
money=0
for v1,v2 in A:
  if v2=="JPY":money+=float(v1)
  else:money+=380000*float(v1)
print(money)