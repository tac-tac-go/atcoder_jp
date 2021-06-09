n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
result=0
for i in range(1,len(xy)):
  result+=abs(xy[i][0]-xy[i-1][0])+abs(xy[i][1]-xy[i-1][1])
print(result)