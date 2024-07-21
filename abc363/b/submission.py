N,T,P = map(int,input().split())
arr = sorted(map(int,input().split()))[::-1]
fil_length = sum([1 for i in arr if i>=T])
if fil_length>=P:
  print(0)
else:
  print(T-arr[P-1])
  

