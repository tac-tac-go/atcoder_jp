n = int(input())
count = [0]*n
for i in range(n-1):
  a, b = map(int, input().split())
  count[a-1] += 1
  count[b-1] += 1
print("Yes") if max(count) == n-1 else print("No")
