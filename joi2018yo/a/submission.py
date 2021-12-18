import math
n,a,b,c,d = map(int,input().split())
print(min(b*math.ceil(n/a),d*math.ceil(n/c)))
