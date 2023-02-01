n,m = map(int,input().split())
array1 = [input()[-3:] for i in range(n)]
array2 = [input()[-3:] for i in range(m)]
count = 0
for i in array1:
  for j in array2:
    if i==j:
      count +=1
      break
print(count)
