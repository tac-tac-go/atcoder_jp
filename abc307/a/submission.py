n = int(input())
array = list(map(int,input().split()))
result = []
count = 0
for i in range(n):
  result.append(str(sum(array[count:count+7])))
  count+=7
print(" ".join(result))

  
  
