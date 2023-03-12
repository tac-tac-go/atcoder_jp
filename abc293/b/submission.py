n = int(input())
array = list(map(int,input().split()))
count = [0]*n
for index,v in enumerate(array):
  if count[index]==0:
    count[v-1]+=1
result = [i+1 for i,v in enumerate(count) if v==0]
print(len(result))
print(" ".join(map(str,result)))
  
  

