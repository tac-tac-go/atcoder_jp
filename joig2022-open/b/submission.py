n = int(input())
array = list(map(int,input().split()))
count=0
for i in range(0,len(array)-2):
  for j in range(i+1,len(array)-1):
    for k in range(j+1, len(array)):
      if array[i]*array[j]==array[k]:
        count+=1
print(count)
      
  
