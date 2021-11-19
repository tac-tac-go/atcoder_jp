n,k = map(int,input().split())
a = n
for i in range(k):
  g1 = "".join(sorted(list(str(a)),reverse=True))
  g2 = g1[::-1]
  g1 = int(g1)
  g2 = int(g2)
  a = g1 - g2
print(a)