N,M = map(int,input().split())
R = [list(map(int,input().split())) for i in range(N+M)]
for i in range(N):
  result=[]
  point=1
  for j in range(N,M+N):
    x1=R[i][0]
    x2=R[j][0]
    y1=R[i][1]
    y2=R[j][1]
    result.append((point,abs(x1-x2)+abs(y1-y2)))
    point+=1
  print(sorted(result,key=lambda x:(x[1],x[0]))[0][0])