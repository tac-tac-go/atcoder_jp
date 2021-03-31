n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
result=[]
for i in range(n):
  result.append(ab[i][0]+ab[i][1])
for i in range(n):
  for j in range(n):
    if i!=j:
      result.append(max(ab[i][0],ab[j][1]))
print(min(result))