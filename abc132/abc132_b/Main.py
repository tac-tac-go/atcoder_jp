N = int(input())
P = list(map(int,input().split()))
count=0
for i in range(1,N-1):
  sort_list = sorted([P[i-1],P[i],P[i+1]])
  if sort_list[1]==P[i]:count+=1
print(count)
