n = int(input())
for i in range(n):
  n_i = int(input())
  array = list(map(int,input().split()))
  print(len(list(filter(lambda x:x%2==1,array))))
  
