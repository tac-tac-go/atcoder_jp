array = [[1],[1,1],[1,2,1],[1,3,3,1]]
n = int(input())
if n >3:
  for i in range(4,n):
    sub_a = [1]
    for j in range(1,i):
      sub_a.append(array[i-1][j]+array[i-1][j-1])
    sub_a.append(1)
    array.append(sub_a)
  for i in range(n):
    print(*array[i])
	
else:
  for i in range(n):
    print(*array[i])
