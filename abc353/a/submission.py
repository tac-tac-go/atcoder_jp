n = int(input())
arr = list(map(int,input().split()))
result = -1
for i in range(1,len(arr)):
  if arr[0]<arr[i]:
    result=i+1
    break
print(result)

