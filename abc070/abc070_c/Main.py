import math
from functools import reduce
numbers = [int(input()) for i in range(int(input()))]
x = reduce(lambda x,y:(x * y) // math.gcd(x, y), numbers, 1)
print(x)