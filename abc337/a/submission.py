n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
x_sum = sum([i for i,_ in xy])
y_sum = sum([j for _,j in xy])
if x_sum>y_sum:
  print("Takahashi")
elif x_sum<y_sum:
  print("Aoki")
else:
  print("Draw")
