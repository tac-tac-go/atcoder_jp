import math
P = int(input())
count = 0
for i in range(10, 0, -1):
  X = math.factorial(i)
  while P >= X:
    P -= X
    count += 1
print(count)
