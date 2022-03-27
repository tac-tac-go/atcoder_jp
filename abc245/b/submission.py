n = int(input())
array = list(map(int,input().split()))
for i in range(0,max(array)+2):
  if i not in array:
    print(i)
    break
