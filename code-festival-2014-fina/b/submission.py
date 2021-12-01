s = list(map(int, list(input())))
result = 0
for i, v in enumerate(s):
  if (i+1) % 2 == 1:
    result += v
  else:
    result -= v
print(result)
