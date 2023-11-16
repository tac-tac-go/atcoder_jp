import re
n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(1,n+1):
  for j in range(1,arr[i-1]+1):
    if re.match('^([0-9])\\1+$',str(i)+str(j)):
      count += 1
print(count)
    
