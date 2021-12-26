import math
a,b = map(int,input().split())
print(0) if a>=b else print(math.ceil((b-a)/10))
