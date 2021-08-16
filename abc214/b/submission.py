s, t = map(int, input().split())
result = []
for i1 in range(101):
  for i2 in range(101):
    for i3 in range(101):
      if i1+i2+i3 <= s:
        result.append([i1, i2, i3])
count = 0
for a, b, c in result:
  if a*b*c <= t:
    count += 1
print(count)
