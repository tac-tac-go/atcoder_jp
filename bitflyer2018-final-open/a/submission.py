n = int(input())
result = []
for _ in range(n):
  s = input()[::-1]
  result.append(min([i for i, si in enumerate(s) if si != "0"]))
print(min(result))
