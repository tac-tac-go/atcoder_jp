n, a, b = map(int, input().split())
t = [int(input()) for i in range(n)]
count = 0
for ti in t:
  if not(ti >= a and ti < b):
    count += 1
print(count)
