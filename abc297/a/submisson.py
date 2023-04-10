n,d = map(int,input().split())
result = -1
array = list( map(int,input().split()))
for i in range(len(array)-1):
  if array[i+1]-array[i]<=d:
    result = array[i+1]
    break
print(result)

