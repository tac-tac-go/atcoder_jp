n = int(input())
xn = list(map(int, input().split()))
count = 10**10
for i in range(min(xn), max(xn)+1):
  if count > sum(map(lambda x: (x-i)**2, xn)):
    count = sum(map(lambda x: (x-i)**2, xn))
print(count)
