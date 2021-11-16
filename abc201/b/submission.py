n = int(input())
data = []
for i in range(n):
  s, t = input().split()
  t = int(t)
  data.append([t, s])
data.sort(reverse=True)
print(data[1][1])
