n, x, y, z = map(int, input().split())
ab = [map(int, input().split()) for i in range(n)]
count = 0
for a, b in ab:
  if (a >= x and b >= y) and (a+b >= z):
    count += 1
print(count)
