n = int(input())
a = sorted(map(int, input().split()))
count = 0
for i in range(n-1):
  count += max(a[i], a[i+1])
count += a[0]
count += a[-1]
count += n
print(count)
