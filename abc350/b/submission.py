n,q = map(int,input().split())
t_arr = list(map(int,input().split()))
n_arr = [1]*n
for i in t_arr:
  if n_arr[i-1]:
    n_arr[i-1]=0
  else:
    n_arr[i-1]=1
print(sum(n_arr))
  

