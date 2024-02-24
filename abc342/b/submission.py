n = int(input())
p_a = list(map(int,input().split()))
q = int(input())
ab_arr = [map(int,input().split()) for i in range(q)]
for a,b in ab_arr:
  if p_a.index(a)>p_a.index(b):
    print(b)
  else:
    print(a)
