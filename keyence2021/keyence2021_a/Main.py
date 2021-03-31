n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_max = 0
c = 0
for i in range(n):
  a_max = max(a_max,a[i])
  c = max(c,a_max * b[i])
  print(c)