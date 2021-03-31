from collections import defaultdict
N,M = map(int,input().split())
result = defaultdict(int)
for i in range(N):
  result[i+1]=0
for i in range(M):
  a,b = map(int,input().split())
  result[a]+=1
  result[b]+=1
result = sorted(result.items(),key=lambda x:x[0])
[print(v) for i,v in result]