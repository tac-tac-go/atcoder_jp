n = int(input())
arr_1 = [list(input()) for i in range(n)]
arr_2 = [list(input()) for i in range(n)]

for row,(i1,j1) in enumerate(zip(arr_1,arr_2)):
  for column,(i2,j2) in enumerate(zip(i1,j1)):
    if i2!=j2:
      print(row+1,column+1)
      break
  else:
    continue
  break
      
