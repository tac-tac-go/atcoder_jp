h,w = map(int,input().split())
array = [list(input()) for i in range(h)]
position = [(i,j)  for i in range(0,h) for j in range(0,w) if array[i][j]=="o"]
print(abs(position[0][0]-position[1][0])+abs(position[0][1]-position[1][1]))
