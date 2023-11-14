x,y = map(int,input().split())
flag = False
if x < y and y-x<=2 or x > y and x-y<=3:
  flag = True
print("Yes") if flag else print("No")
  
