n = int(input())
t = list(map(int,input().split()))
m = int(input())
px = [map(int,input().split()) for i in range(m)]
for p,x in px:
  t_c = t.copy()
  t_c[p-1]=x
  print(sum(t_c))