n,x,y,z = map(int,input().split())
print("Yes") if min(x,y)<=z and max(x,y)>=z else print("No")
