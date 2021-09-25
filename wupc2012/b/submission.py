n = int(input())
a = [input() for _ in range(n)]
b = []
for i in range(n):
  for j in range(n):
    if i != j:
      b.append(a[i]+a[j])
b.sort()
print(b[0])
