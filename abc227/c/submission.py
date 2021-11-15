n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
count = 0
for i1 in range(1, n-1):
  for i2 in range(i1+1, n):
      for i3 in range(i2+1, n+1):
          point = [xy[i1-1], xy[i2-1], xy[i3-1]]
          point.sort()
          point1 = point[0]
          point2 = point[1]
          point3 = point[2]
          dx2 = point3[0]-point1[0]
          dx1 = point2[0]-point1[0]
          dy1 = point2[1]-point1[1]
          dy2 = point3[1]-point1[1]
          if dx2*dy1 != dx1*dy2:
            count += 1
print(count)
