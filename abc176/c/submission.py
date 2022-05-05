n = int(input())
array = list(map(int,input().split()))
max_v = array[0]
count = 0
for i in range(1,len(array)):
  if max_v > array[i]:
    count+= (max_v-array[i])
  else:
    max_v = array[i]
print(count)

