import math
n, a = map(int, input().split())
team = n//3
print(math.ceil(a/3), team if a >= team else a)
