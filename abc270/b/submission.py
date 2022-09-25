x, y, z = map(int, input().split())
if y < 0:
    x = - x
    y = - y
    z = - z

if x < y:
    exit(print(abs(x)))

if z > y:
    exit(print(-1))

print(abs(x - z) + abs(z))

