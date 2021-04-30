import math
x,y = map(int,input().split())
print(-1) if x%y==0 else print((x * y // math.gcd(x, y))-x)
