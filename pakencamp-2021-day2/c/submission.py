n,m = map(int,input().split())
a_array = list(map(int,input().split()))
b_array = list(map(int,input().split()))
result = list(set(b_array) -  (set(a_array) & set(b_array)))
if len(result)==0:
  print(0)
else:
  print(len(result))
  [print(i) for i in result]

