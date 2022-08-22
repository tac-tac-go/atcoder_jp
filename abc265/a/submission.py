x,y,n = map(int,input().split())
p1 = x*n
p2 = ((n//3)*y+(n%3)*x)
print(min(p1,p2))
