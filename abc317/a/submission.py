N,H,X = map(int,input().split())
p_arr = list(map(int,input().split()))
min_v =  10**9
result = 0
for index,i in enumerate(p_arr):
  if H+i>=X:
    if min_v>H+i:
      min_v = H+i
      result = index+1
print(result)
